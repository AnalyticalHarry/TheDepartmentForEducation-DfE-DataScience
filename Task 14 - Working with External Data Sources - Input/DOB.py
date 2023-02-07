#This content variable store string data types
contents = "" 

# Open the text  file
f = open('DOB.txt', 'r+') 

#Creating a for loop to iterate through line, and displays each item.
for line in f:
    contents = contents + line

    #using split() built-in function to split word into list data types
    splitted_contents = contents.split(',') 

#Display "Name" on the screen
print('Name')
#creating for loop to iterate data through "splitted_contents"
for i in splitted_contents:
    #Display list of name
    print(i)
#Display "Birthdate" on the screen
print('Birthdate:')
#creating for loop to iterate valuethrough "splitted_contents"
for j in splitted_contents:
    data = j.split()
    #Display "Birthday" on the screen
    print(" ".join(data[2:]))