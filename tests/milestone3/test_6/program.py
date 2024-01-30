# DYNAPYT: DO NOT INSTRUMENT


import dynapyt.runtime as _rt

_dynapyt_ast_ = "/home/liln/23w_program_analysis/myproject/Dynamic_Slicing_DynaPyt/tests/milestone3/test_6/program.py" + ".orig"
try:
    class Person:
        def __init__(self, name):
            self.name = _rt._write_(_dynapyt_ast_, 2, _rt._read_(_dynapyt_ast_, 1, lambda: name), [lambda: self.name])
                
    def slice_me():
        p = _rt._write_(_dynapyt_ast_, 6, _rt._call_(_dynapyt_ast_, 5, _rt._read_(_dynapyt_ast_, 4, lambda: Person), False, [("", 'Nobody')], {}), [lambda: p])
        indefinite_pronouns = _rt._write_(_dynapyt_ast_, 7, ['Everybody', 'Somebody', 'Nobody', 'Anybody'], [lambda: indefinite_pronouns])
        if _rt._enter_if_(_dynapyt_ast_, 13, _rt._attr_(_dynapyt_ast_, 9, _rt._read_(_dynapyt_ast_, 8, lambda: p), "name") in _rt._read_(_dynapyt_ast_, 10, lambda: indefinite_pronouns)):
            _rt._call_(_dynapyt_ast_, 11, print, False, [("", "A person's name should not be an indefinite pronoun.")], {})
            p.name = _rt._write_(_dynapyt_ast_, 12, "Undefined", [lambda: p.name])
        tries_left = _rt._write_(_dynapyt_ast_, 14, 3, [lambda: tries_left])
        while _rt._enter_while_(_dynapyt_ast_, 23, (_rt._attr_(_dynapyt_ast_, 16, _rt._read_(_dynapyt_ast_, 15, lambda: p), "name") in _rt._read_(_dynapyt_ast_, 17, lambda: indefinite_pronouns) or _rt._attr_(_dynapyt_ast_, 19, _rt._read_(_dynapyt_ast_, 18, lambda: p), "name") == "Undefined") and _rt._read_(_dynapyt_ast_, 20, lambda: tries_left) > 0):
            _rt._call_(_dynapyt_ast_, 21, print, False, [("", "Choose a proper name")], {})
            tries_left -= _rt._aug_assign_(_dynapyt_ast_, 22, lambda: tries_left, 12, 1)
        return _rt._attr_(_dynapyt_ast_, 25, _rt._read_(_dynapyt_ast_, 24, lambda: p), "name") # slicing criterion
    
    _rt._call_(_dynapyt_ast_, 27, _rt._read_(_dynapyt_ast_, 26, lambda: slice_me), False, [], {})
except Exception as _dynapyt_exception_:
    _rt._catch_(_dynapyt_exception_)
