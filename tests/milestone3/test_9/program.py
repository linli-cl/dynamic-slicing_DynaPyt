# DYNAPYT: DO NOT INSTRUMENT


import dynapyt.runtime as _rt

_dynapyt_ast_ = "/home/liln/23w_program_analysis/myproject/Dynamic_Slicing_DynaPyt/tests/milestone3/test_9/program.py" + ".orig"
try:
    def slice_me():
        operation = _rt._write_(_dynapyt_ast_, 1, "sum", [lambda: operation])
        a = _rt._write_(_dynapyt_ast_, 2, 10, [lambda: a])
        b = _rt._write_(_dynapyt_ast_, 3, 15, [lambda: b])
        if _rt._enter_if_(_dynapyt_ast_, 8, _rt._read_(_dynapyt_ast_, 4, lambda: operation) == "sum"):
            c = _rt._write_(_dynapyt_ast_, 7, _rt._read_(_dynapyt_ast_, 5, lambda: a) + _rt._read_(_dynapyt_ast_, 6, lambda: b), [lambda: c]) # slicing criterion
        if _rt._enter_if_(_dynapyt_ast_, 13, _rt._read_(_dynapyt_ast_, 9, lambda: operation) == "sub"):
            c = _rt._write_(_dynapyt_ast_, 12, _rt._read_(_dynapyt_ast_, 10, lambda: a) - _rt._read_(_dynapyt_ast_, 11, lambda: b), [lambda: c])
            
    _rt._call_(_dynapyt_ast_, 15, _rt._read_(_dynapyt_ast_, 14, lambda: slice_me), False, [], {})
except Exception as _dynapyt_exception_:
    _rt._catch_(_dynapyt_exception_)
