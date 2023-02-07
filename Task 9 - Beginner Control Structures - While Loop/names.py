#"name_list" variable is a list data structure, which will stored all variable enter by user
name_list = []

#while loop will activate without any specific condition
while True:
    #"user_input" variable will store string varible, which will input take from user
    user_input = str(input("Please enter name: "))
    #append() built-in function has been used for storing all strinf value in "name_list" list data structure
    name_list.append(user_input)
    #if "user_input" variable store "stop" or user enter "stop" than, string comparsion take place, break will work
    # if "user_input" is equal to "stop", then it will break loop
    if user_input == "stop":
        break
#last string data "stop" will be removed usinf pop()
name_list.pop()
print("\nList of name:",name_list)