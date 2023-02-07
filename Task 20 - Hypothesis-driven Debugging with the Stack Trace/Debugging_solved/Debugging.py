#defining function "print_values_of"
def print_values_of(dictionary, keys):
    #creating for loop to iterate in keys
    for key in keys:
        #prinitng output
        print(dictionary[key])
#dictonary with string values
#bug one was "homer": 'd'oh', which meant to be "homer": 'd\'oh'
#bug two was missing exclamation mark "!" and desired output'd\'oh!'
simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": 'd\'oh!', "maggie": " (Pacifier Suck)"}

#calling function with two arguments.
#bug three was not using list data types to pass arguments
print_values_of(simpson_catch_phrases, ["lisa", "bart", "homer"])