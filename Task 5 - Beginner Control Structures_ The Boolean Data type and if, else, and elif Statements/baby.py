#int() function has been used for user input, this function only allow integers to pass
#birth_year varibale will store integer value and it is basically user birth year
birth_year = int(input("Please enter your birth year: "))

#User_year varibale store difference of current year (2022) and user birth year
#user_year store integer value, which will be a user age
user_year = 2022 - birth_year

#if statement is used to check, user is truly 18+ or not
#if user_year value is greater than 18, than statement is True and it will print out "Congrates, you are old enough"
if user_year>18:
    print("\nCongrates, you are old enough")
    
#else statement is opposite of if statement. non qualifying value or False statement will be passed to this lane.
#if user_year value is less than 18, than it will print out "Sorry, you aren't old enough"
else:
    print("\nSorry, you aren't old enough")