class Person:
    def __init__(self, name):
        self.name = name
            
def slice_me():
    p = Person('Nobody')
    indefinite_pronouns = ['Everybody', 'Somebody', 'Nobody', 'Anybody']
    if p.name in indefinite_pronouns:
        p.name = "Undefined"
    return p.name # slicing criterion

slice_me()