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


def negate_odd_ifs(code: str) -> str:
    syntax_tree = cst.parse_module(code)
    wrapper = cst.metadata.MetadataWrapper(syntax_tree)
    code_modifier = OddIfNegation()
    new_syntax_tree = wrapper.visit(code_modifier)
    return new_syntax_tree.code

def remove_lines(code: str, lines_to_keep : List[int]) -> str:
    print('-----------------------------------------------------------')
    tree = cst.parse_module(code)
    wrapper = cst.metadata.MetadataWrapper(tree)
    ranges = wrapper.resolve(cst.metadata.PositionProvider)
    # for n in dir(ranges):        
    #     print(eval('ranges.'+n))
    #     print(n)
    # print(dir(ranges))

    for i,j in ranges.items():
        if str(j.start.line) in lines_to_keep:
            #print('-------------------------',j.start.line,'-------------------------')
            if type(i).__name__ in ['SimpleStatementLine','Comparison','name']:
                print(tree.code_for_node(i))
    #         #print(dir(i))
    # #print(ranges.values())
    # print(dir(tree.body[0]))
    # print(tree.BaseSmallStatement)
    print(tree.code, '++++++++++++++++')

    return tree.code
        
    
    
