# DYNAPYT: DO NOT INSTRUMENT


import dynapyt.runtime as _rt

_dynapyt_ast_ = "/home/liln/23w_program_analysis/myproject/Dynamic_Slicing_DynaPyt/tests/milestone3/test_7/program.py" + ".orig"
try:
    class Person:
        def __init__(self, name):
            self.name = _rt._write_(_dynapyt_ast_, 2, _rt._read_(_dynapyt_ast_, 1, lambda: name), [lambda: self.name])
            self.age = _rt._write_(_dynapyt_ast_, 3, 0, [lambda: self.age])

        def increase_age(self, years):
            self.age += _rt._aug_assign_(_dynapyt_ast_, 8, lambda: _rt._attr_(_dynapyt_ast_, 6, _rt._read_(_dynapyt_ast_, 5, lambda: self), "age"), 0, _rt._read_(_dynapyt_ast_, 7, lambda: years))
                
    def slice_me():
        p = _rt._write_(_dynapyt_ast_, 12, _rt._call_(_dynapyt_ast_, 11, _rt._read_(_dynapyt_ast_, 10, lambda: Person), False, [("", 'Nobody')], {}), [lambda: p])
        while _rt._enter_while_(_dynapyt_ast_, 18, _rt._attr_(_dynapyt_ast_, 14, _rt._read_(_dynapyt_ast_, 13, lambda: p), "age") < 18):
            _rt._call_(_dynapyt_ast_, 17, _rt._attr_(_dynapyt_ast_, 16, _rt._read_(_dynapyt_ast_, 15, lambda: p), "increase_age"), False, [("", 1)], {})
        if _rt._enter_if_(_dynapyt_ast_, 26, _rt._attr_(_dynapyt_ast_, 20, _rt._read_(_dynapyt_ast_, 19, lambda: p), "age") == 18):
            _rt._call_(_dynapyt_ast_, 25, print, False, [("", f'{_rt._attr_(_dynapyt_ast_, 22, _rt._read_(_dynapyt_ast_, 21, lambda: p), "name")} is {_rt._attr_(_dynapyt_ast_, 24, _rt._read_(_dynapyt_ast_, 23, lambda: p), "age")}')], {})
        return _rt._read_(_dynapyt_ast_, 27, lambda: p) # slicing criterion
    
    _rt._call_(_dynapyt_ast_, 29, _rt._read_(_dynapyt_ast_, 28, lambda: slice_me), False, [], {})
except Exception as _dynapyt_exception_:
    _rt._catch_(_dynapyt_exception_)
