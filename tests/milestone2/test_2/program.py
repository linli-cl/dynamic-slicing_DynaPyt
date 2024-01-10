# DYNAPYT: DO NOT INSTRUMENT


import dynapyt.runtime as _rt

_dynapyt_ast_ = "/home/liln/23w_program_analysis/myproject/Dynamic_Slicing_DynaPyt/tests/milestone2/test_2/program.py" + ".orig"
try:
    def slice_me():
        x = _rt._write_(_dynapyt_ast_, 1, 10, [lambda: x])
        y = _rt._write_(_dynapyt_ast_, 3, _rt._read_(_dynapyt_ast_, 2, lambda: x), [lambda: y])
        z = _rt._write_(_dynapyt_ast_, 5, _rt._read_(_dynapyt_ast_, 4, lambda: x) * 2, [lambda: z]) # slicing criterion
    
    _rt._read_(_dynapyt_ast_, 6, lambda: slice_me)()
except Exception as _dynapyt_exception_:
    _rt._catch_(_dynapyt_exception_)
