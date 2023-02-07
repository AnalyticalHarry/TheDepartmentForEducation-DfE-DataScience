name_list = [] #name_list list data type will store list of name
while True: #while loop for running continous loop
    user_name = str(input("Enter user name: ").title()) #user_name varibale will take input from user
     #user_sensitivity will convert all small starting letter to capital like "harry" will be "Harry"
    #title() built in function has been used
    user_sensitivity = user_name.title() 
    if user_name == "John": #if user_name is equal to "John" than their will be break of while loop
        break
    else:
        name_list.append(user_sensitivity)#all names will be stored into name_List using append() built in function
print("Incorrect names: ",name_list)#printing result