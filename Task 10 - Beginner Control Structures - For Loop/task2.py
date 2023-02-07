#"user_year"  variable will store  integer value and input() builtin fucntion has been used to take input from user.
user_year = int(input("\nWhat year you want to start with? ")) #user will input year 
#"year_number" variable will store integer value and input() builtin function has been used to take input from user
year_number = int(input("\nHow many years do you  want to check? ")) #user will input number of year
print()# empty print() has been used to make gap between print statement
#for loop with range 
#range initial point will be "user_year" value and final point will be "user_year"+"year_number"
for i in range(user_year, (user_year+year_number)):
    #control flow statement for checking leap year
    #if user input is leap year than if statement will ork
    if (i % 400 == 0) or (i % 100 != 0 and i %4 == 0): 
        print(i,"is a leap year.")#print command for showing leap year
    else:
    #else statement will be applicable, when it isnt leap year
        print(i,"isn't a leap year.")#print command for showing not a leap year
