# DYNAPYT: DO NOT INSTRUMENT


import dynapyt.runtime as _rt

_dynapyt_ast_ = "/home/liln/23w_program_analysis/myproject/Dynamic_Slicing_DynaPyt/tests/milestone3/test_10/program.py" + ".orig"
try:
    def slice_me():
        ages = _rt._write_(_dynapyt_ast_, 1, [0, 25, 50, 75, 100, 150], [lambda: ages])
        current_age = _rt._write_(_dynapyt_ast_, 4, _rt._sub_(_dynapyt_ast_, 3, _rt._read_(_dynapyt_ast_, 2, lambda: ages), [0]), [lambda: current_age]) # slicing criterion
        while _rt._enter_while_(_dynapyt_ast_, 9, _rt._read_(_dynapyt_ast_, 5, lambda: current_age) < _rt._sub_(_dynapyt_ast_, 7, _rt._read_(_dynapyt_ast_, 6, lambda: ages), [-1])):
            current_age += _rt._aug_assign_(_dynapyt_ast_, 8, lambda: current_age, 0, 1)
        if _rt._enter_if_(_dynapyt_ast_, 17, _rt._read_(_dynapyt_ast_, 10, lambda: current_age) == _rt._sub_(_dynapyt_ast_, 12, _rt._read_(_dynapyt_ast_, 11, lambda: ages), [-1])):
            ages[-1] += _rt._aug_assign_(_dynapyt_ast_, 15, lambda: _rt._sub_(_dynapyt_ast_, 14, _rt._read_(_dynapyt_ast_, 13, lambda: ages), [-1]), 0, 50)
        else:
            _rt._call_(_dynapyt_ast_, 16, print, False, [("", "something went wrong")], {})        
        return _rt._read_(_dynapyt_ast_, 18, lambda: ages)
    
    _rt._call_(_dynapyt_ast_, 20, _rt._read_(_dynapyt_ast_, 19, lambda: slice_me), False, [], {})
except Exception as _dynapyt_exception_:
    _rt._catch_(_dynapyt_exception_)
