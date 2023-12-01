class Person:
    def __init__(self, name):
        self.name = name
            
def slice_me():
    p = Person('Nobody')
    indefinite_pronouns = ['Everybody', 'Somebody', 'Nobody', 'Anybody']
    if p.name in indefinite_pronouns:
        print("A person's name should not be an indefinite pronoun.")
        p.name = "Undefined"
    tries_left = 3
    while (p.name in indefinite_pronouns or p.name == "Undefined") and tries_left > 0:
        print("Choose a proper name")
        tries_left -= 1
    return p.name # slicing criterion

slice_me()