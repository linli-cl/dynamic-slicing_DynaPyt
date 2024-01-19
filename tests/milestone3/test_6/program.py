# DYNAPYT: DO NOT INSTRUMENT


import dynapyt.runtime as _rt

_dynapyt_ast_ = "/home/liln/23w_program_analysis/myproject/Dynamic_Slicing_DynaPyt/tests/milestone3/test_6/program.py" + ".orig"
try:
    class Person:
        def __init__(self, name):
            self.name = _rt._write_(_dynapyt_ast_, 2, _rt._read_(_dynapyt_ast_, 1, lambda: name), [lambda: self.name])
                
    def slice_me():
        p = _rt._write_(_dynapyt_ast_, 5, _rt._read_(_dynapyt_ast_, 4, lambda: Person)('Nobody'), [lambda: p])
        indefinite_pronouns = _rt._write_(_dynapyt_ast_, 6, ['Everybody', 'Somebody', 'Nobody', 'Anybody'], [lambda: indefinite_pronouns])
        if _rt._enter_if_(_dynapyt_ast_, 11, _rt._attr_(_dynapyt_ast_, 8, _rt._read_(_dynapyt_ast_, 7, lambda: p), "name") in _rt._read_(_dynapyt_ast_, 9, lambda: indefinite_pronouns)):
            print("A person's name should not be an indefinite pronoun.")
            p.name = _rt._write_(_dynapyt_ast_, 10, "Undefined", [lambda: p.name])
        tries_left = _rt._write_(_dynapyt_ast_, 12, 3, [lambda: tries_left])
        while _rt._enter_while_(_dynapyt_ast_, 20, (_rt._attr_(_dynapyt_ast_, 14, _rt._read_(_dynapyt_ast_, 13, lambda: p), "name") in _rt._read_(_dynapyt_ast_, 15, lambda: indefinite_pronouns) or _rt._attr_(_dynapyt_ast_, 17, _rt._read_(_dynapyt_ast_, 16, lambda: p), "name") == "Undefined") and _rt._read_(_dynapyt_ast_, 18, lambda: tries_left) > 0):
            print("Choose a proper name")
            tries_left -= _rt._aug_assign_(_dynapyt_ast_, 19, lambda: tries_left, 12, 1)
        return _rt._attr_(_dynapyt_ast_, 22, _rt._read_(_dynapyt_ast_, 21, lambda: p), "name") # slicing criterion
    
    _rt._read_(_dynapyt_ast_, 23, lambda: slice_me)()
except Exception as _dynapyt_exception_:
    _rt._catch_(_dynapyt_exception_)
