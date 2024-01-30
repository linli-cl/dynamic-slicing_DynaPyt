# DYNAPYT: DO NOT INSTRUMENT


import dynapyt.runtime as _rt

_dynapyt_ast_ = "/home/liln/23w_program_analysis/myproject/Dynamic_Slicing_DynaPyt/tests/milestone3/test_8/program.py" + ".orig"
try:
    def slice_me():
        hour = _rt._write_(_dynapyt_ast_, 1, 0, [lambda: hour])
        greeting = _rt._write_(_dynapyt_ast_, 2, "", [lambda: greeting])
        german_greetings = _rt._write_(_dynapyt_ast_, 3, ['Guten Morgen', 'Guten Tag', 'Guten Abend', 'Gute Nacht'], [lambda: german_greetings])
        while _rt._enter_while_(_dynapyt_ast_, 18, _rt._read_(_dynapyt_ast_, 4, lambda: hour) < 24):
            if _rt._enter_if_(_dynapyt_ast_, 10, _rt._read_(_dynapyt_ast_, 5, lambda: hour) < 12):
                greeting = _rt._write_(_dynapyt_ast_, 8, _rt._sub_(_dynapyt_ast_, 7, _rt._read_(_dynapyt_ast_, 6, lambda: german_greetings), [0]), [lambda: greeting])
                return _rt._read_(_dynapyt_ast_, 9, lambda: greeting) # slicing criterion
            if _rt._enter_if_(_dynapyt_ast_, 16, _rt._read_(_dynapyt_ast_, 11, lambda: hour) > 12 and _rt._read_(_dynapyt_ast_, 12, lambda: hour) < 17):
                greeting = _rt._write_(_dynapyt_ast_, 15, _rt._sub_(_dynapyt_ast_, 14, _rt._read_(_dynapyt_ast_, 13, lambda: german_greetings), [1]), [lambda: greeting])
            hour += _rt._aug_assign_(_dynapyt_ast_, 17, lambda: hour, 0, 1)
        return _rt._read_(_dynapyt_ast_, 19, lambda: greeting)
    
    _rt._call_(_dynapyt_ast_, 21, _rt._read_(_dynapyt_ast_, 20, lambda: slice_me), False, [], {})
except Exception as _dynapyt_exception_:
    _rt._catch_(_dynapyt_exception_)
