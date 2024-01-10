# DYNAPYT: DO NOT INSTRUMENT


import dynapyt.runtime as _rt

_dynapyt_ast_ = "/home/liln/23w_program_analysis/myproject/Dynamic_Slicing_DynaPyt/tests/milestone2/test_7/program.py" + ".orig"
try:
    class Person:
        def __init__(self, name):
            self.name = _rt._write_(_dynapyt_ast_, 2, _rt._read_(_dynapyt_ast_, 1, lambda: name), [lambda: self.name])
                
    def slice_me():
        p = _rt._write_(_dynapyt_ast_, 5, _rt._read_(_dynapyt_ast_, 4, lambda: Person)('Nobody'), [lambda: p])
        indefinite_pronouns = _rt._write_(_dynapyt_ast_, 6, ['Everybody', 'Somebody', 'Anybody'], [lambda: indefinite_pronouns])
        _rt._attr_(_dynapyt_ast_, 8, _rt._read_(_dynapyt_ast_, 7, lambda: indefinite_pronouns), "append")(_rt._attr_(_dynapyt_ast_, 10, _rt._read_(_dynapyt_ast_, 9, lambda: p), "name"))
        return _rt._attr_(_dynapyt_ast_, 12, _rt._read_(_dynapyt_ast_, 11, lambda: p), "name") # slicing criterion
    
    _rt._read_(_dynapyt_ast_, 13, lambda: slice_me)()
except Exception as _dynapyt_exception_:
    _rt._catch_(_dynapyt_exception_)
