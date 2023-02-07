#user input for interger value
#numerical value  will be store in user_name
user_number = int(input("Enter an integer: "))

# if and elif statement for divisble by 2 and 5
if  user_number%2==0 and user_number%5==0:
    print("\n1. User enter number is divisible by 2 and 5")
elif user_number%2!=0 and user_number%5!=0:
    print("\n1. User enter number is not divisble by 2 and 5")
    
#if and else statement for divisble by 2 or 5
if  user_number%2==0:
    print("\n2. User enter number is divisible by 2")
else:
    print("\n2. User enter number is not divisible by 2")        
if user_number%5==0:
    print("\n2. User enter number is divisble by 5")
else:
    print("\n2. User enter number is not divisble by 5")

#if and elif statemenet for divisible or not divisble by 2 or 5
if user_number%2==0 or user_number%5==0:
    print("\n3. User enter number is divisible by 2 or 5 ")
elif user_number%2!=0 or user_number%5!=0:
    print("\n3. User enter number is not divisible by 2 or 5")
