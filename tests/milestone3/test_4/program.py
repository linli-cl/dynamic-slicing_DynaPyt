# DYNAPYT: DO NOT INSTRUMENT


import dynapyt.runtime as _rt

_dynapyt_ast_ = "/home/liln/23w_program_analysis/myproject/Dynamic_Slicing_DynaPyt/tests/milestone3/test_4/program.py" + ".orig"
try:
    def slice_me():
        ages = _rt._write_(_dynapyt_ast_, 1, [0, 25, 50, 75, 100], [lambda: ages])
        smallest_age = _rt._write_(_dynapyt_ast_, 4, _rt._sub_(_dynapyt_ast_, 3, _rt._read_(_dynapyt_ast_, 2, lambda: ages), [0]), [lambda: smallest_age])
        middle_age = _rt._write_(_dynapyt_ast_, 7, _rt._sub_(_dynapyt_ast_, 6, _rt._read_(_dynapyt_ast_, 5, lambda: ages), [2]), [lambda: middle_age])
        highest_age = _rt._write_(_dynapyt_ast_, 10, _rt._sub_(_dynapyt_ast_, 9, _rt._read_(_dynapyt_ast_, 8, lambda: ages), [-1]), [lambda: highest_age])
        new_highest_age = _rt._write_(_dynapyt_ast_, 13, _rt._read_(_dynapyt_ast_, 11, lambda: middle_age) + _rt._read_(_dynapyt_ast_, 12, lambda: highest_age), [lambda: new_highest_age])
        _rt._call_(_dynapyt_ast_, 17, _rt._attr_(_dynapyt_ast_, 15, _rt._read_(_dynapyt_ast_, 14, lambda: ages), "append"), False, [("", _rt._read_(_dynapyt_ast_, 16, lambda: new_highest_age))], {})
        for age in _rt._gen_(_dynapyt_ast_, 22, _rt._read_(_dynapyt_ast_, 18, lambda: ages)):
            if _rt._enter_if_(_dynapyt_ast_, 21, _rt._read_(_dynapyt_ast_, 19, lambda: age) == 150):
                _rt._call_(_dynapyt_ast_, 20, print, False, [("", "Bye!")], {})
        return _rt._read_(_dynapyt_ast_, 23, lambda: ages) # slicing criterion
    
    _rt._call_(_dynapyt_ast_, 25, _rt._read_(_dynapyt_ast_, 24, lambda: slice_me), False, [], {})
except Exception as _dynapyt_exception_:
    _rt._catch_(_dynapyt_exception_)
