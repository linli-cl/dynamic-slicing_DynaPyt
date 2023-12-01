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

    def leave_If(self, original_node: If, updated_node: If) -> BaseStatement | FlattenSentinel[BaseStatement] | RemovalSentinel:
        location = self.get_metadata(PositionProvider, original_node) 
        #print('location.start.line',location.start.line)
        if location.start.line % 2 == 0:
            return updated_node
        negated_test = cst.UnaryOperation(
            operator=cst.Not(),
            expression=updated_node.test,
        )
        return updated_node.with_changes(
            test=negated_test,    #how to know the name of the change?
        )

def negate_odd_ifs(code: str) -> str:
    syntax_tree = cst.parse_module(code)
    wrapper = cst.metadata.MetadataWrapper(syntax_tree)
    code_modifier = OddIfNegation()
    new_syntax_tree = wrapper.visit(code_modifier)
    return new_syntax_tree.code


def remove_lines(code: str, lines_to_keep : List[int]) -> str:

    class RemoveLines(cst.CSTTransformer):
        METADATA_DEPENDENCIES = ( PositionProvider,)
        def __init__(self, lines_to_keep):
            self.lines_to_keep = lines_to_keep
        def on_leave(self, original_node:"CSTNode", updated_node: "CSTNode" ) -> Union["CSTNode", RemovalSentinel]:
            location = self.get_metadata(PositionProvider, original_node)
            if isinstance(updated_node, cst.SimpleStatementLine) and str(location.start.line) not in self.lines_to_keep:
                return cst.RemoveFromParent()
            else:
                return updated_node

    syntax_tree = cst.parse_module(code)
    wrapper = cst.metadata.MetadataWrapper(syntax_tree)
    code_modifier = RemoveLines(lines_to_keep)
    new_syntax_tree = wrapper.visit(code_modifier)

    return new_syntax_tree.code
