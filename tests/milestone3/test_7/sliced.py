class Person:
    def __init__(self, name):
        self.name = name
        self.age = 0
    def increase_age(self, years):
        self.age += years
def slice_me():
    p = Person('Nobody')
    while p.age < 18:
        pass
    if p.age == 18:
        pass
    return p # slicing criterion
slice_me()