class Person:
    def __init__(self, name):
        self.name = name

def slice_me():
    p1 = Person('Nobody')
    p2 = p1
    indefinite_pronouns = ['Everybody', 'Somebody', 'Nobody', 'Anybody']
    p2.name = indefinite_pronouns[1]
    return p1 # slicing criterion

slice_me()