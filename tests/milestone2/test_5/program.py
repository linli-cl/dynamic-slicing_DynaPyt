# DYNAPYT: DO NOT INSTRUMENT


import dynapyt.runtime as _rt

_dynapyt_ast_ = "/home/liln/23w_program_analysis/myproject/Dynamic_Slicing_DynaPyt/tests/milestone2/test_5/program.py" + ".orig"
try:
    def slice_me():
        ages = _rt._write_(_dynapyt_ast_, 1, [0, 25, 50, 75, 100], [lambda: ages])
        smallest_age = _rt._write_(_dynapyt_ast_, 4, _rt._sub_(_dynapyt_ast_, 3, _rt._read_(_dynapyt_ast_, 2, lambda: ages), [0]), [lambda: smallest_age])
        middle_age = _rt._write_(_dynapyt_ast_, 7, _rt._sub_(_dynapyt_ast_, 6, _rt._read_(_dynapyt_ast_, 5, lambda: ages), [2]), [lambda: middle_age])
        highest_age = _rt._write_(_dynapyt_ast_, 10, _rt._sub_(_dynapyt_ast_, 9, _rt._read_(_dynapyt_ast_, 8, lambda: ages), [-1]), [lambda: highest_age])
        new_highest_age = _rt._write_(_dynapyt_ast_, 13, _rt._read_(_dynapyt_ast_, 11, lambda: middle_age) + _rt._read_(_dynapyt_ast_, 12, lambda: highest_age), [lambda: new_highest_age])
        ages[-1] = _rt._write_(_dynapyt_ast_, 14, 150, [lambda: ages[-1]]) # slicing criterion
        return _rt._read_(_dynapyt_ast_, 15, lambda: ages)
    
    _rt._read_(_dynapyt_ast_, 16, lambda: slice_me)()
except Exception as _dynapyt_exception_:
    _rt._catch_(_dynapyt_exception_)
