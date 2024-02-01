# DYNAPYT: DO NOT INSTRUMENT


import dynapyt.runtime as _rt

_dynapyt_ast_ = "/home/liln/23w_program_analysis/myproject/Dynamic_Slicing_DynaPyt/tests/milestone2/test_13/program.py" + ".orig"
try:
    def slice_me():
        arr = _rt._write_(_dynapyt_ast_, 1, [1, 2, 3, 4, 5], [lambda: arr])
        crr = _rt._write_(_dynapyt_ast_, 2, [1, 2, 3, 4, 5], [lambda: crr])
        brr = _rt._write_(_dynapyt_ast_, 4, _rt._read_(_dynapyt_ast_, 3, lambda: crr), [lambda: brr])
        _rt._attr_(_dynapyt_ast_, 6, _rt._read_(_dynapyt_ast_, 5, lambda: brr), "append")(6)
        _rt._attr_(_dynapyt_ast_, 8, _rt._read_(_dynapyt_ast_, 7, lambda: arr), "pop")(0)
        result = _rt._write_(_dynapyt_ast_, 10, _rt._read_(_dynapyt_ast_, 9, lambda: arr), [lambda: result]) # slicing criterion
        return _rt._read_(_dynapyt_ast_, 11, lambda: result)
    
    _rt._read_(_dynapyt_ast_, 12, lambda: slice_me)()
except Exception as _dynapyt_exception_:
    _rt._catch_(_dynapyt_exception_)
