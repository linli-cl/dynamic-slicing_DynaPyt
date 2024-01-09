import libcst as cst
from dynapyt.analyses.BaseAnalysis import BaseAnalysis
from dynapyt.instrument.IIDs import IIDs
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, Union
from libcst.metadata import (
    PositionProvider,
)
import os

class SliceDataflow(BaseAnalysis):
    def __init__(self, source_path):
        with open(source_path, "r") as file:
            source = file.read()
        iid_object = IIDs(source_path)
        self.source_path = source_path
        self.code = source
        self.comment_line: int
        self.keep_lines=[]
        self.asts = {}
        self.graph={}
        self.slice_results_line=set()
             
    def get_location_name(self,dyn_ast,iid):

        from dynapyt.utils.nodeLocator import get_node_by_location
        location = self.iid_to_location(dyn_ast,iid)
        node = get_node_by_location(self._get_ast(dyn_ast)[0], location)
        codeline=location.start_line
        return node, type(node),codeline
        
    def print_graph(self):
        print('graph:')
        for i,j in self.graph.items():
            print(i,j)

    def begin_execution(self) -> None:
        self.get_line_infomation()
        print('keep_lines',self.keep_lines)
        print('comment_line',self.comment_line) 

    def get_line_infomation(self):  #stupid way
        syntax_tree = cst.parse_module(self.code)
        wrapper = cst.metadata.MetadataWrapper(syntax_tree)
        thepos = wrapper.resolve(PositionProvider)
        otherpart_index=[]
        for i in range(len(wrapper.module.body)):
            if 'FunctionDef' in str(type(wrapper.module.body[i])):
                index1=i
            else:
                print(type(wrapper.module.body[i]))
                otherpart_index.append(i)
        node=wrapper.module.body[index1].body.body

        for i in range(len(node)):
            comment=node[i].trailing_whitespace.comment
            if comment != None:
                location=thepos[node[i]]
                self.comment_line=location.start.line
        
        for i in otherpart_index:
            nodes=wrapper.module.body[i]
            self.keep_lines.append([thepos[nodes].start.line,thepos[nodes].end.line])


    def read(self, dyn_ast: str, iid: int, val: Any) -> Any:
        # print("read",val,type(val))
        a,b,c=self.get_location_name(dyn_ast,iid)
        # print(c)
        #print(c,b,a)
        if c not in self.graph:
            self.graph[c] =  {'write':set(),'read':set(),'addtion':set()}
        if 'libcst._nodes.expression.Name' in str(b):
            self.graph[c]['read'].add(a.value)
        elif 'libcst._nodes.expression.Attribute' in str(b):
            if a.attr.value == 'append'or a.attr.value == 'pop': # modify
                self.graph[c]['write'].add(a.value.value)
            else:
                self.graph[c]['read'].add(a.value.value)
        else:
            pass
        
    def write(
        self, dyn_ast: str, iid: int, old_vals: List[Callable], new_val: Any
    ) -> Any:
        a,b,c=self.get_location_name(dyn_ast,iid)
        #print(c,b,a)
        if c not in self.graph:
            self.graph[c] =  {'write':set(),'read':set(),'addtion':set()}

        if 'libcst._nodes.statement.Assign' in str(b):
            if type(a.targets[0].target.value) is str:
                self.graph[c]['write'].add(a.targets[0].target.value)
            else:
                self.graph[c]['write'].add(a.targets[0].target.value.value)
            if 'libcst._nodes.expression.Subscript' in  str(type(a.targets[0].target)):
                self.graph[c]['read'].add(a.targets[0].target.value.value)
        elif 'libcst._nodes.statement.AugAssign' in str(b):
            self.graph[c]['write'].add(a.target.value)
        else:
            pass

        # for addition test
        from pathlib import Path
        path=Path(self.source_path)
        func_name=str(path.parent.name)+'.'
        if func_name in str(type(new_val)) or 'list' in str(type(new_val)):
            try:
                
                if isinstance(a.value.value,str):   
                    self.graph[c]['addtion'].add(a.value.value) 
            except Exception as e:
                
                pass

    def slicepoint(self,graph_line,slice_point):
        self.slice_results_line.add(graph_line[0])
        #print(graph_line,self.slice_results_line,'------',graph_line[1:])
        for j in slice_point:
            for k in range(1,len(graph_line)):
                if j in self.graph[graph_line[k]]['write']:
                    self.slicepoint(graph_line[k:],self.graph[graph_line[k]]['read'])
                    
        
    def end_execution(self) -> None:
        self.print_graph()
        graph_line=[i for i in reversed(self.graph.keys())]
        begin_slice_line=graph_line.index(self.comment_line)   
        graph_line=graph_line[begin_slice_line:]

        slice_point=self.graph[graph_line[0]]['read']
        self.slice_results_line.add(graph_line[0])
        self.slicepoint(graph_line[0:],slice_point)
        # print('slice_results_line',self.slice_results_line)

        # Addtion test:
        for i in self.graph:
            if self.graph[i]['addtion'] != set():
                # print(i,self.graph[i]['addtion'])
                templist= [x for x in self.slice_results_line if x < i]
                if templist != []:
                    for j in range(len(graph_line)):
                        if self.graph[graph_line[j]]['write']==self.graph[i]['write']:
                            self.slicepoint(graph_line[j:],self.graph[graph_line[j]]['read'])
        #print('--')
        for i in self.keep_lines:
            for j in range(i[0],i[1]+1):
                #print(j)
                self.slice_results_line.add(j)
        #print('slice_results_line',self.slice_results_line)
        print()
        lines_to_keep=[str(i) for i in self.slice_results_line]
        code=self.remove_lines(self.code,lines_to_keep)
        self.write_to_file(code)

    def remove_lines(self, code: str, lines_to_keep : List[int]) -> str:

        class RemoveLines(cst.CSTTransformer):
            METADATA_DEPENDENCIES = ( PositionProvider,)
            def __init__(self, lines_to_keep):
                self.lines_to_keep = lines_to_keep
            def on_leave(self, original_node:"CSTNode", updated_node: "CSTNode" ) :#-> Union["CSTNode", RemovalSentinel]:
                location = self.get_metadata(PositionProvider, original_node)
                if isinstance(updated_node, cst.SimpleStatementLine) and str(location.start.line) not in self.lines_to_keep:
                    return cst.RemoveFromParent()
                elif isinstance(updated_node,cst.EmptyLine):
                    return cst.RemoveFromParent()
                else:
                    return updated_node
        syntax_tree = cst.parse_module(code)
        #print(syntax_tree)
        wrapper = cst.metadata.MetadataWrapper(syntax_tree)
        code_modifier = RemoveLines(lines_to_keep)
        new_syntax_tree = wrapper.visit(code_modifier)

        return new_syntax_tree.code

    def write_to_file( self,code: str) -> str:
        with open(os.path.dirname(self.source_path)+'/sliced.py','w') as f:
            f.write(code)
