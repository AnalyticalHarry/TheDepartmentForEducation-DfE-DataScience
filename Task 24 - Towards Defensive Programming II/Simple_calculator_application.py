#Defining function for calculations
def calculation(number1, number2, operation):
    #addition
    if operation == "+":
        #return addition of two numbers
        return number1 + number2
    #subtraction
    elif operation == "-":
        #return subtraction of two numbers
        return number1 - number2
    #division 
    elif operation == "/":
        #error handeling for division 
        try:
            #formula for division
            division_result =  number1/number2
            #return division result
            return division_result
        #if numerator is zero, than it is zero division error
        except ZeroDivisionError:
            #return message on screen "Cannot divide by zero"
            division_result = "Cannot divide by zero"
            return division_result
    #multiplication
    elif operation == "*":
        #return multiplication of two numbers
        return number1*number2
    else:
        #If user enter invalid character than, "Invalid Input" will be printed on screen
        print("Invalid Input")
        
        
        
#defining main function  
def main_function():
    try:
        #user input first number
        number1 = float(input("Enter the number one: ")) 
    except ValueError:
        print("Invalid Input")
    
    try:
        #user input second number
        number2 = float(input("Enter the number two: "))
        
    except ValueError:
        print("Invalid Input")
        
    try:
        #user assign operator
        operation = str(input("Enter operation (+, -, / or *): "))
    
    except SyntaxError as error:
        print("Invalid Syntax")

    try:
        #calling calculation function
        result = calculation(number1, number2, operation)
        #printing result on screen
        print(f"\nResult of {number1} {operation} {number2} = {result}\n")
    
    #it will pass UnboundLocalError
    except UnboundLocalError as Error:
        pass
    
    try:
        #naming file output as "calculations.txt"
        filename = input("Enter filename to save: ")
            # writing the equation and result to a filename
        with open(filename+".txt", "a") as file: #append only mode
            #writing result
            file.write(f"{number1} {operation} {number2} = {result}\n")
            
    #it will pass UnboundLocalError
    except UnboundLocalError as Error:
        pass
        
#calling calculation function
main_function()
    
#list of result stored from calculations.txt file
equations = []
#error catching
try:
    #opening file
    file_input = input("Enter file name to open: ")
    with open(file_input+".txt", 'r') as file:
        #creating for loop to iterate in file
        for line in file:
            #storing string values to above list "equations"
            equations.append(line.strip())
#execute when their is an exception, normally if file dosen't exist
except FileNotFoundError:
        #if file dosen't exist, it will print this message on screen
        print("The file that you are trying to open doesn't exist")

#space in line
print()
#for loop for indexing and printing list of data
for i,j in enumerate (equations):
    print(i,j)