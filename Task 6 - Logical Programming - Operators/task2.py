#Importing library
import math


#user will input three specific word at a time, "square","rectangle", and "round"
#if user input square, it  will follow the path of square if statement for calculating area
#if user input rectangle, it will follow the path of rectangle  if statement for calculating area
#if user input round, it will follow the path of round, if statement for calculating circle
user_input = str(input("Enter any one \"square\", \"rectangle\", or \"round\" :" ))

#if statement for square
#it will compare string "square" and if it True, it will ask user to input l value
if user_input == "square":
    #l stand for length of square
    l = float(input("\nInput:\nEnter length for square: "))
    #def function for re-usibility 
    def square(l):
        area = l**2 #area  of square
        return area #value return to caller
    result = square(l) #function square call and saved in variable result
    #f-string for presenting value and projecting varible "square_solution"
    print(f"\nOutput:\nArea of square: {result}") 
    
#if statement for rectangle
#it will compare string "rectangle" and if it True, it will ask user to input l and w value
if  user_input == "rectangle":
    #l stand for length
    #w stand for width
    l = float(input("\nInput:\nEnter length for rectangle: "))
    w = float(input("Enter width for rectangle: "))
    def rectangle(l,w):
        area= l*w #area of rectangle
        return area #valuereturn to caller
    result  = rectangle(l,w) #function rectangle call and saved in varibale result
    print(f"\nOutput:\nArea of rectangle: {result}")
    
    
#if statement for square
#it will compare string "round" and if it True, it will ask user to input r value    
if user_input == "round":
    #importing library
    
    #changing math.pi to pie
    r = float(input("\nInput:\nEnter the radius of circle: "))
    def circle(r):
        area = math.pi*(r**2) #area of circle
        return area 
    result = circle(r) #storing into variable result
    print(f"\nOutput:\nArea of circle: {round(result,2)}")