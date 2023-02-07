#num1 variable store value of 10
num1 = 10
#num2 variable store value of 20
num2 = 20
#num3 variable store value of 30
num3 = 30
#if statement, num2 is greater than equal to num1
if num2>=num1:
    print("\nnum2 is greater than num1")
#else statement if num1 is greater than num2
else:
    print("\nnum1 is greater than num2")
#if statement, number is even number
if num1%2 == 0:
    print("\nnum1 is an Even number")
#else statement, if number is odd
else:
    print("\nnum1 is  an Odd number")
#########################################################################################################################################################################
#########################################################################################################################################################################
print("\n")
#This is a code for conditional statement to sort the three numbers for largest to smallest


#user input varibale are num1, num2 and num3
#input()built-in function has been used
#int() built-in function has been used for denoting specific value to store
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

#def function has been used due to re-use property
#num1,num2 and num3 are declared parameter in function
def numplay(num1, num2, num3):
#if statement if num is greater than equal to num2 and  num1 greater than equal to num3
    if num1>=num2 and num1>=num3:
        #if num2 is greater than equal to  num3
        if num2>=num3:
                print("\nnum1 is the first largest number",num1)
                print("\nnum2 is the second largest number", num2)
                print("\nnum3 is the third lowest number", num3)
#if statement num2 is greater than equal to num1, and num2 is greater and equal to num3
    if num2>=num1 and num2>=num3:
        #if num3 is greater and equal to num1
        if num3>=num1:
                print("\nnum2 is the first largest number",num2)
                print("\nnum3 is the second largest number", num3)
                print("\nnum1 is the lowest  number", num1)
#if statement num3 is greater than equal to num3 is greater than equal to  num2
    if num3>=num1 and num3>=num2:
        #if num3 is greater than equal to num3 and num2 is greater than num1
        if num3>=num2 and num2>num1:
                print("\nnum3 is the first largest number", num3)
                print("\nnum2 is the second largest number",num2)
                print("\nnum1 is the lowest number", num1)
#if statement num1 is greater than equal to num2 and num1 is greater than equal to num3
    if num1>=num2 and num1>=num3:
        #if num2 is less than equal to num3
        if num2<=num3:
                print("\nnum1 is the first largets number", num1)
                print("\nnum3 is the second largest number",  num3)
                print("\nnum2 is the lowest number",num2)
#if statement num2 is greater than equalto num1,and num2 is greater than equal to num3
    if num2>=num1 and num2>=num3:
        #if num1 is greater than equal to num3 and num3 is less than qual to num2
        if num1>=num3 and num3<=num2:
                print("\nnum2 is the first largest number", num2)
                print("\nnum1 is the second largest number", num1)
                print("\nnum3 is the lowest number", num3)
#if statement, num3 is greater than equal to num2 and num1 is greater than equal to num2
    if num3>= num2 and num1>=num2:
        #if statement, num1 is less than equal to num3 and num1 is greater than equal to num2
        if num1<=num3 and num1>=num2:
            print("\nnum3 is the first largest number", num3)
            print("\nnum1 is the second largest number", num1)
            print("\nnum2 is the lowest  number",num2)
#functional call
numplay(num1, num2, num3)



print("num1 = 10, num2 = 20, and num3 = 30\n")
a = numplay(10,20,30)
print("\n-----------------------------------")
print("num1 = 10, num2 = 30, and num3 = 20\n")
b = numplay(10,30,20)
print("\n-----------------------------------")
print("num1 = 20, num2 = 10, and num3 = 30\n")
c = numplay(20,10,30)
print("\n-----------------------------------")
print("num1 = 20, num2 = 30, and num3 = 10\n")
d = numplay(20,30,10)
print("\n-----------------------------------")
print("num1 = 30, num2 = 20, and num3 = 10\n")
e = numplay(30,20,10)
print("\n-----------------------------------")
print("num1 = 30, num2 = 10, and num3 = 20\n")
f = numplay(30,10,20)
print("\n-----------------------------------")