# DYNAPYT: DO NOT INSTRUMENT


import dynapyt.runtime as _rt

_dynapyt_ast_ = "/home/liln/23w_program_analysis/myproject/Dynamic_Slicing_DynaPyt/tests/milestone3/test_2/program.py" + ".orig"
try:
    def slice_me():
        x = _rt._write_(_dynapyt_ast_, 1, 1, [lambda: x])
        y = _rt._write_(_dynapyt_ast_, 2, 2, [lambda: y])
        z = _rt._write_(_dynapyt_ast_, 3, 3, [lambda: z])
        if _rt._enter_if_(_dynapyt_ast_, 7, _rt._read_(_dynapyt_ast_, 4, lambda: x) > 4):
            z += _rt._aug_assign_(_dynapyt_ast_, 5, lambda: z, 0, 2)
        else:
            y -= _rt._aug_assign_(_dynapyt_ast_, 6, lambda: y, 12, 5)
        return _rt._read_(_dynapyt_ast_, 8, lambda: y) # slicing criterion
    
    _rt._call_(_dynapyt_ast_, 10, _rt._read_(_dynapyt_ast_, 9, lambda: slice_me), False, [], {})
except Exception as _dynapyt_exception_:
    _rt._catch_(_dynapyt_exception_)
