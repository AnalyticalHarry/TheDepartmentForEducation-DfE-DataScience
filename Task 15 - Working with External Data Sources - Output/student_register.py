#This line of code will ask user to enter number of student to register
total_students = int(input("Enter the number of students: "))

#"total_students" list will store, total number of student ID 
student_id =[]

#for loop for repeating task 
for i in range(0, total_students):
    
    #"user_input" will ask to enter student ID
    user_input = input("Enter student ID: ")
    
    #append() built in function will help to store all user input into list "student_id"
    student_id.append(user_input+ "\n"+"."*30)
    
#This will print "Total Number of student registered:" on screen
print("\nTotal Number of student registered: ")

#this will index all student id from 1 to total number of student user entered for registeration
for i,j in enumerate (student_id):
    print(i+1,j)

#write only, it will create a file in the dosen't exist and for existing file, the data is overwritten
with open("reg_form.txt", "w") as output:
    for row in student_id:
        output.write(str(row)+ "\n")
#this is for closing file
output.close()