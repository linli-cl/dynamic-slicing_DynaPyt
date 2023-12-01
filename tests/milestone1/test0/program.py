# DYNAPYT: DO NOT INSTRUMENT


import dynapyt.runtime as _rt

_dynapyt_ast_ = r"C:\Users\thisi\OneDrive\文档\BaiduSyncdisk\23w\3.program analysis\exercises\project\project\dynamicslicing\tests\milestone1\test0\program.py" + ".orig"
try:
    def slice_me():
        x = _rt._write_(_dynapyt_ast_, 1, 5, [lambda: x])
        print(_rt._str_(_dynapyt_ast_, 2, "Hello World"))
        if x < 10:
            x += _rt._aug_assign_(_dynapyt_ast_, 3, lambda: x, 0, 5)
            y = _rt._write_(_dynapyt_ast_, 4, 0, [lambda: y])
        return y
    
    slice_me()
except Exception as _dynapyt_exception_:
    _rt._catch_(_dynapyt_exception_)
