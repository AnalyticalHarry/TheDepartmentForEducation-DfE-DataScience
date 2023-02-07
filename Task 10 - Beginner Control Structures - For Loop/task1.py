#user_input is a varibale which will store int value
user_input = int(input("\nEnter the number for table: ")) #User will enter table of choice
#print(), empty print command has been used for making space in ouput
print()
#Nested loop has been used to interate between range of "user_input" value and 13
for i in range(1,13):
    for j in range(user_input,13):
        #f-string for creating multiplication between two numerical variable i and j
        print(f"{j} * {i} = {i*j}")
        if j==user_input: #condition if j value becomes equal to "user_input" value than,it will activate break 
            break