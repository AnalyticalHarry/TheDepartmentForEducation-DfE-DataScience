def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[k])

simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": 'd'oh', "maggie": " (Pacifier Suck)"}

print_values_of(simpson_catch_phrases, 'lisa', 'bart', 'homer')

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

