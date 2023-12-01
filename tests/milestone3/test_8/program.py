def slice_me():
    hour = 0
    greeting = ""
    german_greetings = ['Guten Morgen', 'Guten Tag', 'Guten Abend', 'Gute Nacht']
    while hour < 24:
        if hour < 12:
            greeting = german_greetings[0]
            return greeting # slicing criterion
        if hour > 12 and hour < 17:
            greeting = german_greetings[1]
        hour += 1
    return greeting

slice_me()