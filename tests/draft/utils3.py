from typing import List
import libcst as cst
from libcst._flatten_sentinel import FlattenSentinel
from libcst._nodes.statement import BaseStatement, If
from libcst._removal_sentinel import RemovalSentinel
from libcst.metadata import (
    ParentNodeProvider,
    PositionProvider,
)
import libcst.matchers as m


class OddIfNegation(m.MatcherDecoratableTransformer):
    """
    Negate the test of every if statement on an odd line.
    """
    METADATA_DEPENDENCIES = (
        ParentNodeProvider,
        PositionProvider,
    )

    def leave_If(self, original_node: If, updated_node: If) -> BaseStatement | FlattenSentinel[BaseStatement] | RemovalSentinel:
        location = self.get_metadata(PositionProvider, original_node)
        if location.start.line % 2 == 0:
            return updated_node
        negated_test = cst.UnaryOperation(
            operator=cst.Not(),
            expression=updated_node.test,
        )
        return updated_node.with_changes(
            test=negated_test,
        )
    
class OddIfNegation2(m.MatcherDecoratableTransformer):
    """
    Negate the test of every if statement on an odd line.
    """
    METADATA_DEPENDENCIES = (
        ParentNodeProvider,
        PositionProvider,
    )

    def __init__(self, nodeline):
        self.nodeline = nodeline

    def leave_If(self,updated_node) -> BaseStatement | FlattenSentinel[BaseStatement] | RemovalSentinel:
        #location = self.get_metadata(PositionProvider, code)
        #print('location.start.line',location.start.line)

        if str(self.nodeline) in self.lines_to_keep:
            print(self.nodeline)
            return updated_node
        negated_test = cst.UnaryOperation(
            operator=cst.Not(),
            expression=updated_node.test,
        )
        return updated_node.with_changes(
            test=negated_test,
        )


def negate_odd_ifs(code: str) -> str:
    syntax_tree = cst.parse_module(code)
    wrapper = cst.metadata.MetadataWrapper(syntax_tree)
    code_modifier = OddIfNegation()
    new_syntax_tree = wrapper.visit(code_modifier)
    return new_syntax_tree.code

def remove_lines(code: str, lines_to_keep : List[int]) -> str:
    
    syntax_tree = cst.parse_module(code)
    wrapper = cst.metadata.MetadataWrapper(syntax_tree)
    ranges = wrapper.resolve(cst.metadata.PositionProvider)
    print(dir(wrapper))
    for i,j in ranges.items():
        nodeline=j.start.line
        if str(j.start.line) not in lines_to_keep:
            code_modifier = OddIfNegation2(nodeline)
            new_syntax_tree = wrapper.visit(code_modifier)
            print(new_syntax_tree.code)
    print()
    print(lines_to_keep)
    print('---------------------------------------------------------------------',new_syntax_tree.code)
    print()
    return new_syntax_tree.code
    
