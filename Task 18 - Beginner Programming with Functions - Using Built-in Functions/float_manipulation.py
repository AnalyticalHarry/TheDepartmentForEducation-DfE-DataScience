#Importing math
import math

#"numbers" will store all user input
numbers = []
#creating for loop for runnning 10times
for  i in range(10):
    #user can enter float number 
    user_number = float(input("Please enter number:" ))
    #"user_number" will be stored in "numbers"
    numbers.append(user_number)
#sapce between print line
print()
#indexing of numbers been input by user
for index, item in enumerate(numbers):
    print(index, item)


#Output result total of all numbers
print(f"The Total of all numbers {sum(numbers)}")

#####################################################################################################################

#indexing numbers 
max = numbers[0]
#initial index is declared zero
index = 0
#for loop to iterate on range between 1 to length og numbers
for i in range(1,len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
        index = i
#printing result of maximum index and maximum float value user has entered 
print(f'Index of maximum value {index} and value is {numbers[index]}')


#####################################################################################################################

#indexing numbers 
min = numbers[0]
#initial index is declared zero
index = 0
#for loop to iterate on range between 1 to length og numbers
for i in range(1,len(numbers)):
    if numbers[i] < min:
        min = numbers[i]
        index = i
#printing result of maximum index and maximum float value user has entered 
print(f'Index of minimum value {index} and value is {numbers[index]}')

######################################################################################################################

# values is a list of all values
def average(numbers): 
    #formula for calculating average value
      return sum(numbers)/len(numbers)
#stroing result as variable
result_average = average(numbers)
#indexing result
average = [result_average][0]
#printing output as average of numbers
print(f"Average of numbers: {round(average, 2)}")

######################################################################################################################

#sorting numbers
numbers.sort()
#declaring median zero
median = 0
#check even numbers
if len(numbers)%2 == 0:
    #formula for even
    x = (len(numbers))/2
    y = (len(numbers)/2) + 1
    median = (x+y)/2
    print("n is even")
#condition for odd numbers
else:
    #formula for odd
    median = (len(numbers)+1)//2
    print("n is odd")
#printing result
if (len(numbers) % 2 != 0):
    print(numbers[median-1])
elif (len(numbers) % 2 == 0):
    #using math floor modules to round up lower point value
    print((numbers[math.floor(median)-1]+numbers[math.floor(median)])/2)