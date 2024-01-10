# DYNAPYT: DO NOT INSTRUMENT


import dynapyt.runtime as _rt

_dynapyt_ast_ = "/home/liln/23w_program_analysis/myproject/Dynamic_Slicing_DynaPyt/tests/milestone2/test_3/program.py" + ".orig"
try:
    def slice_me():
        x = _rt._write_(_dynapyt_ast_, 1, 1, [lambda: x])
        y = _rt._write_(_dynapyt_ast_, 2, 2, [lambda: y])
        x = _rt._write_(_dynapyt_ast_, 5, _rt._read_(_dynapyt_ast_, 3, lambda: x) + _rt._read_(_dynapyt_ast_, 4, lambda: y), [lambda: x]) # slicing criterion
        y += _rt._aug_assign_(_dynapyt_ast_, 6, lambda: y, 0, 2)
        return _rt._read_(_dynapyt_ast_, 7, lambda: y)
    
    _rt._read_(_dynapyt_ast_, 8, lambda: slice_me)()
except Exception as _dynapyt_exception_:
    _rt._catch_(_dynapyt_exception_)
