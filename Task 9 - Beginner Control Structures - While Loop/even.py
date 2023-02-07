#"user_number" variable will store int value
#intput() built function has been used for taking input from user
user_number = int(input("\nEnter your number:"))
#number is declared zero
#initial vlaue of number is zero
number = 2
#while loop only iterate even number
while number<=user_number:
    #every iteration 2 will be added
    number = number + 2
    #while presenting output will print command, every iteration 2 is subtracted
    print(number-2)