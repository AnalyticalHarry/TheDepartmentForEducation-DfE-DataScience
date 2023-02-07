numbers = [] #Varibale numbers is a list data types which are storing three digit integers
#For loop for taking input of three different integers 
#input are number 1 = 20, number 2 = 75, and number 3 = 35
for i in range(3):
    user_number = int(input("Enter your number: "))
    numbers.append(user_number)
            
#The sum of all the numbers
summation = sum(numbers)

#The sum of all the numbers
subtraction = numbers[0]-numbers[1]

#The Third number multiplied by the first number
multiplication = numbers[2]*numbers[1]

#The sum of all three numbers divided by the third number
division = summation/numbers[2]

print("\nThree different integers list:", numbers,"\n")
print("\n1. The Sum of all the numbers: ",summation)
print("\n2. The first number minus the second numbers: ",subtraction)
print("\n3. The Third number multiplied by the first number: ",multiplication)
print("\n3. The Third number multiplied by the first number: ",(round(division,2)))