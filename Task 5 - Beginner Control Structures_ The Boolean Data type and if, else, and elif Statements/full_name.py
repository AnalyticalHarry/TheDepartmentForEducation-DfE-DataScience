#input() function has been used to store user fullname into variable user_name
#string data type will be stored into varibale user_name
#title() function has been used to capitalised the first letter of user input
user_name = input("Enter your Full Name: ").title()
if len(user_name) == 0:
    print("\nYou haven't entered anything. Please enter your full name\n")
    print("Output: ",user_name)
elif len(user_name) < 4:
    print("\nYou have entered less than 4 characters. Please make sure that you have entered your name and surname\n")
    print("Output: ",user_name)
elif len(user_name) > 25:
    print("\nYou have entered more than 25 characters, Please make sure that you have only entered your full name\n")
    print("Output: ",user_name)
else:
    print("\nThank you for entering your name\n")
    print("Output: ",user_name)