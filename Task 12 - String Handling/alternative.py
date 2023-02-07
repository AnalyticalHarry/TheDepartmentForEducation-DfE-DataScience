#"string" variable will store string data types "Hello World"
string = "Hello World"
#presentation of original format of string using f-string print function
print(f"\nOriginal string: {string}")

#alt stand for alternate variable which will store string data types
alt = ""
#for loop for iterating inside the string length
for i in range(len(string)):
    #if and else statemnt for alternating upper and lower case string
    
    #if statement, it will convert every second iterated value into lower case
    if i % 2 != 0: 
        alt = alt + string[i].lower()
    #else statement, it work opposite to if statement. it will convert all value into lower case after upper case character, for maintaing alternative characters
    else:
        alt = alt + string[i].upper()
#Ouput or final result 
print(f"\nAlternate string: {alt}")



########################################################################################################################################
#"string" variable will store string data types "Hello World"
string = "I am learning to code"
#presentation of original format of string using f-string print function
print(f"\nOriginal string: {string}")
#alt stand for alternate variable which will store string data types
alt  = " "
operation_split = string.split()
for i in range(len(operation_split)):
    if i%2 != 0:
        alt = alt +" "+ operation_split[i].upper()
    else:
        alt = alt +" "+ operation_split[i].lower()
#Ouput or final result 
print(f"\nAlternate string:{alt}")