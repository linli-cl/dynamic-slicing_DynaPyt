# DYNAPYT: DO NOT INSTRUMENT


import dynapyt.runtime as _rt

_dynapyt_ast_ = "/home/liln/23w_program_analysis/myproject/Dynamic_Slicing_DynaPyt/tests/milestone2/test_10/program.py" + ".orig"
try:
    def slice_me():
        german_greetings = _rt._write_(_dynapyt_ast_, 1, ['Hallo', 'Guten Morgen'], [lambda: german_greetings])
        english_greetings = _rt._write_(_dynapyt_ast_, 2, ['Hello', 'Good morning'], [lambda: english_greetings])
        translation = _rt._write_(_dynapyt_ast_, 7, f"{_rt._sub_(_dynapyt_ast_, 4, _rt._read_(_dynapyt_ast_, 3, lambda: german_greetings), [0])} is {_rt._sub_(_dynapyt_ast_, 6, _rt._read_(_dynapyt_ast_, 5, lambda: english_greetings), [0])}", [lambda: translation])
        print(_rt._read_(_dynapyt_ast_, 8, lambda: translation))
        # This is the translation of Hello, World!
        greeting = _rt._write_(_dynapyt_ast_, 11, f"{_rt._sub_(_dynapyt_ast_, 10, _rt._read_(_dynapyt_ast_, 9, lambda: german_greetings), [0])}, Welt!", [lambda: greeting])
        return _rt._read_(_dynapyt_ast_, 12, lambda: greeting) # slicing criterion
    
    _rt._read_(_dynapyt_ast_, 13, lambda: slice_me)()
except Exception as _dynapyt_exception_:
    _rt._catch_(_dynapyt_exception_)
