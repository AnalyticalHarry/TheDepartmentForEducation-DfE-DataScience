print("Sentence for example: The quick brown fox jumps over the lazy dog.")#Printing instruction
user_string = str(input("Please enter your sentence: ")) #user_string will store string value and input() built in function has been used

alphabet = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] #disappear_word list data types has stored a,e,i,o,u for  small case and A,E,I,O,U for  upper case
result = "" #result or output of string will be stored here

for i in range(len(user_string)): #for loop to iterate into user_string
    if user_string[i] not in alphabet: #comparing user input sentence and alphabet a,e,i,o,u,A,E,I,O,U
        result = result + user_string[i]

print("\nAfter stripping a,e,i,o,u: ", result) #printing result