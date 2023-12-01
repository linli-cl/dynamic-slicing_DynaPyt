from typing import List, Union
import libcst as cst
from libcst._flatten_sentinel import FlattenSentinel
from libcst._nodes.statement import BaseStatement, If
from libcst._removal_sentinel import RemovalSentinel
from libcst.metadata import (
    ParentNodeProvider,
    PositionProvider,
)
import libcst.matchers as m

class OddIfNegation(cst.CSTTransformer):
#class OddIfNegation(m.MatcherDecoratableTransformer):
    """
    Negate the test of every if statement on an odd line.
    """
    METADATA_DEPENDENCIES = (
        ParentNodeProvider,
        PositionProvider,
    )
    def __init__(self, lines_to_keep):
        self.lines_to_keep = lines_to_keep

    # def leave_If(self, original_node: If, updated_node: If) -> BaseStatement | FlattenSentinel[BaseStatement] | RemovalSentinel:
    #     location = self.get_metadata(PositionProvider, original_node) #only 1 location?  4
    #     print('location.start.line',location.start.line)
    #     if location.start.line % 2 == 1:
    #         return cst.RemoveFromParent()#updated_node        
        
    #     negated_test = cst.UnaryOperation(
    #         operator=cst.Not(),
    #         expression=updated_node.test,
    #     )
    #     return updated_node.with_changes(
    #         test=negated_test,    #how to know the name of the change?
    #     )

    def on_leave(self, original_node: If, updated_node: If) -> BaseStatement | FlattenSentinel[BaseStatement] | RemovalSentinel:
        location = self.get_metadata(PositionProvider, original_node)
        if isinstance(updated_node, cst.SimpleStatementLine) and str(location.start.line) not in self.lines_to_keep:
            return cst.RemoveFromParent()
        else:
            return updated_node

def negate_odd_ifs(code: str) -> str:
    syntax_tree = cst.parse_module(code)
    wrapper = cst.metadata.MetadataWrapper(syntax_tree)
    code_modifier = OddIfNegation()
    new_syntax_tree = wrapper.visit(code_modifier)
    return new_syntax_tree.code


def remove_lines(code: str, lines_to_keep : List[int]) -> str:
    # syntax_tree = cst.parse_module(code)
    # print(syntax_tree)
    # wrapper = cst.metadata.MetadataWrapper(syntax_tree)
    # ranges = wrapper.resolve(cst.metadata.PositionProvider)
    # for i,j in ranges.items():
    #     if str(j.start.line) not in lines_to_keep:
    #         print('-------------------------',j.start.line,'-------------------------')
    #         print(type(i))
    #         #print(dir(i))
    #         print(i._is_removable())  #how to get CSTnode?
    #         syntax_tree =syntax_tree.deep_remove(i)
    # print(syntax_tree.code)


# didnt work?
    syntax_tree = cst.parse_module(code)
    wrapper = cst.metadata.MetadataWrapper(syntax_tree)
    code_modifier = OddIfNegation(lines_to_keep)
    new_syntax_tree = wrapper.visit(code_modifier)
    print(new_syntax_tree.code)
    return new_syntax_tree.code
