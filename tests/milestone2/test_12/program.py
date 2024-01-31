# DYNAPYT: DO NOT INSTRUMENT


import dynapyt.runtime as _rt

_dynapyt_ast_ = "/home/liln/23w_program_analysis/myproject/Dynamic_Slicing_DynaPyt/tests/milestone2/test_12/program.py" + ".orig"
try:
    def slice_me():
        arr = _rt._write_(_dynapyt_ast_, 1, [1, 2, 3, 4, 5], [lambda: arr])
        brr = _rt._write_(_dynapyt_ast_, 3, _rt._read_(_dynapyt_ast_, 2, lambda: arr), [lambda: brr])
        _rt._attr_(_dynapyt_ast_, 5, _rt._read_(_dynapyt_ast_, 4, lambda: brr), "append")(6)
        _rt._attr_(_dynapyt_ast_, 7, _rt._read_(_dynapyt_ast_, 6, lambda: arr), "pop")(0)
        result = _rt._write_(_dynapyt_ast_, 9, _rt._read_(_dynapyt_ast_, 8, lambda: arr), [lambda: result]) # slicing criterion
        return _rt._read_(_dynapyt_ast_, 10, lambda: result)
    
    _rt._read_(_dynapyt_ast_, 11, lambda: slice_me)()
except Exception as _dynapyt_exception_:
    _rt._catch_(_dynapyt_exception_)
