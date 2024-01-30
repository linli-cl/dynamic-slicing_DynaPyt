# DYNAPYT: DO NOT INSTRUMENT


import dynapyt.runtime as _rt

_dynapyt_ast_ = "/home/liln/23w_program_analysis/myproject/Dynamic_Slicing_DynaPyt/tests/milestone3/test_1/program.py" + ".orig"
try:
    def slice_me():
        x = _rt._write_(_dynapyt_ast_, 1, 1, [lambda: x])
        y = _rt._write_(_dynapyt_ast_, 2, 2, [lambda: y])
        z = _rt._write_(_dynapyt_ast_, 3, 3, [lambda: z])
        if _rt._enter_if_(_dynapyt_ast_, 6, _rt._read_(_dynapyt_ast_, 4, lambda: x) < 4):
            y += _rt._aug_assign_(_dynapyt_ast_, 5, lambda: y, 0, 2)
        if _rt._enter_if_(_dynapyt_ast_, 9, _rt._read_(_dynapyt_ast_, 7, lambda: x) > 0):
            z -= _rt._aug_assign_(_dynapyt_ast_, 8, lambda: z, 12, 5)
        return _rt._read_(_dynapyt_ast_, 10, lambda: y) # slicing criterion
    
    _rt._call_(_dynapyt_ast_, 12, _rt._read_(_dynapyt_ast_, 11, lambda: slice_me), False, [], {})
except Exception as _dynapyt_exception_:
    _rt._catch_(_dynapyt_exception_)
