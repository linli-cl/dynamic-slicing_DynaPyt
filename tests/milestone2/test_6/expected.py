class Person:
    def __init__(self, name):
        self.name = name

def slice_me():
    p = Person('Nobody')
    return p.name # slicing criterion

slice_me()