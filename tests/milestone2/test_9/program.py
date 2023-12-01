def slice_me():
    german_greetings = ['Hallo', 'Guten Morgen']
    english_greetings = ['Hello', 'Good morning']
    translation = f"{german_greetings[0]} is {english_greetings[0]}"
    greeting = f"{english_greetings[0]}, World!"
    return greeting # slicing criterion

slice_me()