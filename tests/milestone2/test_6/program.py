class Person:
    def __init__(self, name):
        self.name = name

def slice_me():
    p = Person('Nobody')
    indefinite_pronouns = ['Everybody', 'Somebody', 'Nobody', 'Anybody']
    indefinite_name = p.name in indefinite_pronouns
    return p.name # slicing criterion

slice_me()