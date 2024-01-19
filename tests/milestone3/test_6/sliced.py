class Person:
    def __init__(self, name):
        self.name = name
def slice_me():
    p = Person('Nobody')
    indefinite_pronouns = ['Everybody', 'Somebody', 'Nobody', 'Anybody']
    if p.name in indefinite_pronouns:
        p.name = "Undefined"
    while (p.name in indefinite_pronouns or p.name == "Undefined") and tries_left > 0:
        pass
    return p.name # slicing criterion
slice_me()