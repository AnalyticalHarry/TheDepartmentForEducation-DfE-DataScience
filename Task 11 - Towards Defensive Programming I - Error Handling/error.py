#1. Syntax error
#SyntaxError: invalid syntax

#Leaving out a keyword or putting it in the wrong place
#Misspelling a keyword (for example a function or variable name)
#Leaving out an important symbol(such as a colon, comma or parentheses)
#Incorrect indentation
#Leaving an empty block(for example, an if statement containing no intented statements)

user_name = str(input("Enter your user name: ") #missing parentheses
if user_name == "harry" #missing column
    print("\nyou're welcome", user_name)


#IndentationError: expected an indented block
#The IndentationError: expected an indented block error indicates that you have an indentation error in the code block, which is most likely caused by a mix of tabs and spaces
user_name = str(input("Enter your user name: "))
if user_name == "harry":
print("\nyou're welcome", user_name) #incorrect indentation

#####################################################################################################################
#####################################################################################################################
#2. Runtime Error

#TypeError: '>=' not supported between instances of 'str' and 'int'
#If you try to compare a string and an integer, you’ll encounter an error that says “not supported between instances of ‘str’ and ‘int’”.
print("Welcome to Bamboo")
#input need to be str or int
user_age = input("How old are you? ") 

if user_age>=18: #"TypeError: '<' not supported between instances of 'str' and 'int'" occurs when we use a comparison operator between values of type str and int.
    print("You can old enough to enter")
else:
    print("Sorry, you aren't old enough")


#IndexError: list index out of range
#“List index out of range” error occurs in Python when we try to access an undefined element from the list.
print("Shopping list\n")
shopping_list = ["Coat", "Shirt", "Shoes", "Watch", "Tie"]
print(shopping_list[5]) #incorrect indexing


#ZeroDivisionError: division by zero
#"ZeroDivisionError: float division by zero" occurs when we try to divide a floating-point number by 0
alpha = 0
beta = 1
gamma = beta/alpha