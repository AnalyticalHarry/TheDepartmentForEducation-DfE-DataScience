#importing math library
import math
#craeting "num_list" list type data structure for storing multiple value 
num_list = []

#while loop is activated
while True:
    #user will input random number
    #"user_input" variable will store integer values
    user_input = int(input("Please enter number: "))
    #append() built-in function has been used to store all user input value inside "num_list"
    num_list.append(user_input)
    #if "user_input" integer value equal to -1, than loop will break
    if user_input == -1:
        break
#formula for average, which is mean value calculation in statistics 
#Sum of all observation/total number of obesrvation
#+1 need to add on numerator and 1 need to be subtracted on denominator
average = (sum(num_list)+1)/(len(num_list)-1)
print("\nList of number:", average)