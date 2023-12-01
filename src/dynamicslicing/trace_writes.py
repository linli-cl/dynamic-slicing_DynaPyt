# Implement a DynaPyt analysis to trace all writes by printing them to stdout.
from dynapyt.analyses.BaseAnalysis import BaseAnalysis
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, Union

class TraceWrites(BaseAnalysis):
    def __init__(self):
        pass
    
    def write(
        self, dyn_ast: str, iid: int, old_vals: List[Callable], new_val: Any
    ) -> Any:
        print(new_val)
