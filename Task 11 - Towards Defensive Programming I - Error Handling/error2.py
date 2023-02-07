#1. Syntax error
#SyntaxError: invalid syntax

#Leaving out a keyword or putting it in the wrong place
#Misspelling a keyword (for example a function or variable name)
#Leaving out an important symbol(such as a colon, comma or parentheses)
#Incorrect indentation
#Leaving an empty block(for example, an if statement containing no intented statements)

user_name = str(input("Enter your user name: ")) #placing the missing parentheses
if user_name == "harry": #placing the missing column
    print("\nyou're welcome", user_name)


#IndentationError: expected an indented block
user_name = str(input("Enter your user name: "))
if user_name == "harry":
    print("\nyou're welcome", user_name) #correct indentation

#####################################################################################################################
#####################################################################################################################
#2. Runtime Error

#TypeError: '>=' not supported between instances of 'str' and 'int'

print("Welcome to Bamboo")
#using int() to specify user input is integer
user_age = int(input("How old are you? ")) 

if user_age>=18:
    print("You can old enough to enter")
else:
    print("Sorry, you aren't old enough")


#IndexError: list index out of range
print("Shopping list\n")
shopping_list = ["Coat", "Shirt", "Shoes", "Watch", "Tie"]
print(shopping_list[4]) #correct indexing


#ZeroDivisionError: division by zero

#"ZeroDivisionError: float division by zero" occurs when we try to divide a floating-point number by 0. 
# To solve the error, use an if statement to check if the number you are dividing by is not zero, or handle the error in a try/except block.
alpha = 0
beta = 1
try:
    gamma = beta/alpha
except ZeroDivisionError:
    gamma = 0

print(gamma)  #0