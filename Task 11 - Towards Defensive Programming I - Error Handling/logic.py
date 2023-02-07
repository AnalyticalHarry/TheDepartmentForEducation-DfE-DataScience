#A logical error is an error in a program that causes it to operate incorrectly
#A logical error occurs due to a fault in the algorithms
#Logical errors, also known as semantic errors, cause the programme to behave incorrectly but do not usually cause the programme to crash. 
# A programme with logic errors, unlike one with syntax errors, can be run, but it does not function as intended.

#1. Example (Average of number)
num1 = float(input('\nEnter a number: '))
num2 = float(input('\nEnter a number: '))
num3 = float(input('\nEnter a number: '))

#the order of operations in arithmetic (the division is evaluated before addition) 
#the program will not give the correct answer
average = num1+num2+num3/3
print('\nThe average of the numbers is:',average,"\n")
print(average, "Average is incorrect due to logical error, (the division is evaluated before addition) ")


#Example 1 Solved
num1 = float(input('\nEnter a number: '))
num2 = float(input('\nEnter a number: '))
num3 = float(input('\nEnter a number: '))

#tuple has been used due to immutable nature
#the itmes are surrounded by paranthesis for addition of all numbers then division by 3
average = (num1+num2+num3)/3
print('\nThe average of the numbers is:',average)

#############################################################################################################################################################################

#Example 2 (Logical error with if and else statement)
age = int(input("\nWhat is your age? : "))
if age <= 18: #incorrect use of logical operator
    print("\nYou are an adult")
else:
    print("\nYou are not an adult")

#Example 2 solved
age = int(input("\nWhat is your age? : "))
if age >= 18: #correct use of logical operator
    print("\nYou are an adult")
else:
    print("\nYou are not an adult")