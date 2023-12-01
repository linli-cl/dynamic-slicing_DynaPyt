class Person:
    def __init__(self, name):
        self.name = name
            
def slice_me():
    p2 = Person('Nobody')
    indefinite_pronouns = ['Everybody', 'Somebody', 'Nobody', 'Anybody']
    p2.name = indefinite_pronouns[1]
    return p2 # slicing criterion

slice_me()