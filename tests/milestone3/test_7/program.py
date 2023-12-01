class Person:
    def __init__(self, name):
        self.name = name
        self.age = 0

    def increase_age(self, years):
        self.age += years
            
def slice_me():
    p = Person('Nobody')
    while p.age < 18:
        p.increase_age(1)
    if p.age == 18:
        print(f'{p.name} is {p.age}')
    return p # slicing criterion

slice_me()