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
        self.comment_line: int # the line number of the slice criterion
        self.keep_lines=[] # the lines of Class and call of slice_me()
        self.asts = {}
        self.graph={}
        self.slice_results_line=set() # the lines of slice results
             
    def get_location_name(self,dyn_ast,iid):
        '''
        Retrieves the location and name information for a given dynamic ast node and id.
        Returns:
        - Tuple: the node, its type, and its code line.
        '''
        from dynapyt.utils.nodeLocator import get_node_by_location
        location = self.iid_to_location(dyn_ast,iid)
        node = get_node_by_location(self._get_ast(dyn_ast)[0], location)
        codeline=location.start_line
        return node, type(node),codeline
        
    def get_line_infomation(self):  #stupid way # Should this be done like this??
        '''
        Get the line numbers of:
        - 1.comment_line: the number of the line code that are used as slice criterion. 
        - 2.keep_lines: the number of lines of code for used Class and the call code of slice_me() by traversing the location.
        '''
        syntax_tree = cst.parse_module(self.code)
        wrapper = cst.metadata.MetadataWrapper(syntax_tree)
        thepos = wrapper.resolve(PositionProvider)
        otherpart_index=[]
        for i in range(len(wrapper.module.body)):  #including ClassDef, FunctionDef, SimpleStatementLine
            if 'FunctionDef' in str(type(wrapper.module.body[i])): 
                index1=i
            else:
                print(type(wrapper.module.body[i]))
                otherpart_index.append(i)  #save ClassDef, SimpleStatementLine
        node=wrapper.module.body[index1].body.body # get the node of def slice_me()

        for i in range(len(node)):
            comment=node[i].trailing_whitespace.comment
            if comment != None:
                location=thepos[node[i]]
                self.comment_line=location.start.line # 1. the line number of the comment line of slice criterion
        
        for i in otherpart_index:
            nodes=wrapper.module.body[i]
            self.keep_lines.append([thepos[nodes].start.line,thepos[nodes].end.line]) #2.get the lines of Class and call of slice_me()

    def begin_execution(self) -> None:
        '''
        Initiates the execution of the analysis.
        '''
        self.get_line_infomation()
        print('keep_lines',self.keep_lines)
        print('comment_line',self.comment_line) 

    def read(self, dyn_ast: str, iid: int, val: Any) -> Any:
        a,b,c =self.get_location_name(dyn_ast,iid) 
        #print(c,b,a) #for debug

        # Locate the code that meets the conditions
        if c not in self.graph:
            self.graph[c] =  {'write':set(),'read':set(),'addtion':set()}
        if 'libcst._nodes.expression.Name' in str(b):
            self.graph[c]['read'].add(a.value)
        elif 'libcst._nodes.expression.Attribute' in str(b):
            if a.attr.value == 'append'or a.attr.value == 'pop': 
                self.graph[c]['write'].add(a.value.value) # modify the code, so here should be 'write'
            else:
                self.graph[c]['read'].add(a.value.value)
        else:
            pass
        
    def write(
        self, dyn_ast: str, iid: int, old_vals: List[Callable], new_val: Any
    ) -> Any:
        a,b,c=self.get_location_name(dyn_ast,iid) #a,b,c are node, type_node, codeline
        #print(c,b,a)

        if c not in self.graph:
            self.graph[c] =  {'write':set(),'read':set(),'addtion':set()}
        if 'libcst._nodes.statement.Assign' in str(b):
            if type(a.targets[0].target.value) is str:
                self.graph[c]['write'].add(a.targets[0].target.value)
            else:
                self.graph[c]['write'].add(a.targets[0].target.value.value)
            if 'libcst._nodes.expression.Subscript' in  str(type(a.targets[0].target)):
                self.graph[c]['read'].add(a.targets[0].target.value.value) # in test_5, like ages[-1]=150, here should be 'read'
        elif 'libcst._nodes.statement.AugAssign' in str(b):
            self.graph[c]['write'].add(a.target.value)
        else:
            pass

        # For addition test
        from pathlib import Path
        path=Path(self.source_path)
        func_name=str(path.parent.name)+'.'
        # if exist the code like 'p2 = p1', the judgment condition is p1. p1 is a object or list： 
        if func_name in str(type(new_val)) or 'list' in str(type(new_val)): 
            try:
                if isinstance(a.value.value,str):   #if the node exist a.value.value, and it is a str
                    self.graph[c]['addtion'].add(a.value.value) 
            except Exception as e:
                pass

    def print_graph(self):
        '''
        Prints the content of the graph attribute for debugging purposes.
        '''
        print('graph:')
        for i,j in self.graph.items():
            print(i,j)

    def slicepoint(self,graph_line,slice_point):
        '''
        After getting the graph. Use recursion to get slice nodes.
        '''
        self.slice_results_line.add(graph_line[0])
        for j in slice_point:
            for k in range(1,len(graph_line)):
                if j in self.graph[graph_line[k]]['write']:
                    self.slicepoint(graph_line[k:],self.graph[graph_line[k]]['read'])         
        
    def end_execution(self) -> None:
        '''
        Finalizes the execution of the analysis.
        1.Based on the graph, find the lines to be sliced through recursion.
        2.Removes unnecessary lines based on the lines_to_keep and writes the modified code to a new file
        '''
        #self.print_graph()  #print to debug
        graph_line=[i for i in reversed(self.graph.keys())]
        begin_slice_line=graph_line.index(self.comment_line)   
        graph_line=graph_line[begin_slice_line:] # 1.1Recursion from the line of slice criterion

        slice_point=self.graph[graph_line[0]]['read']
        self.slice_results_line.add(graph_line[0])
        self.slicepoint(graph_line[0:],slice_point)

        # 1.2.Recursion for addtion test:
        for i in self.graph:
            if self.graph[i]['addtion'] != set():
                templist= [x for x in self.slice_results_line if x < i]
                if templist != []:
                    for j in range(len(graph_line)):
                        if self.graph[graph_line[j]]['write']==self.graph[i]['write']:
                            self.slicepoint(graph_line[j:],self.graph[graph_line[j]]['read'])

        for i in self.keep_lines: # get the lines of Class(from the start line to the end line) and call of slice_me()
            for j in range(i[0],i[1]+1):
                self.slice_results_line.add(j)
        lines_to_keep=[str(i) for i in self.slice_results_line]

        # 2.Removes unnecessary lines based on the lines_to_keep and writes the modified code to a new file:
        def remove_lines(code: str, lines_to_keep : List[int]) -> str:
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
            wrapper = cst.metadata.MetadataWrapper(syntax_tree)
            code_modifier = RemoveLines(lines_to_keep)
            new_syntax_tree = wrapper.visit(code_modifier)
            return new_syntax_tree.code

        def write_to_file(code: str) -> str:
            with open(os.path.dirname(self.source_path)+'/sliced.py','w') as f:
                f.write(code)
    
        code=remove_lines(self.code,lines_to_keep)
        write_to_file(code)
