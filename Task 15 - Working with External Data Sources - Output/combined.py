#numbers1 conatins list of number from 1 to 10
numbers1 = "1,2,3,4,5,6,7,8,9,10"

#number 2 contains list of number from 11 to 20
numbers2 = "11,12,13,14,15,16,17,18,19,20"

#writing file "numbers1.txt"
with open("numbers1.txt","w") as file_1:
    #for loop in interating numbers1
    for i in numbers1:
        file_1.write(i)

#writing file "numbers2.txt"
with open("numbers2.txt", "w") as file_2:
    #for loop in interating numbers2
    for j in numbers2:
        file_2.write(j)
#opening file into read mode
file_1 = open("numbers1.txt", "r")
file_2 = open("numbers2.txt", "r")

#writing file "all_numbers.txt" 
with open("all_numbers.txt", "w") as file_3:
    #for loop interating into file_1
    for i in file_1:
        #writing into file_3, "all_numbers.txt"
        file_3.write(i)
    #for loop intering into file_2
    for j in file_2:
        #writing into file_3, "all_numbers.txt"
        file_3.write(j)