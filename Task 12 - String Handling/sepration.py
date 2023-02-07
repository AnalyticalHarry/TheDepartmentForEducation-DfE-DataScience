#user_sentence varibale will take input from user
#user_sentence will store string value
#input() builtin function has been udes
user_sentence = str(input("Enter your sentence: "))
print()#spacing in line
words = user_sentence.split()#split() built in function has been used to split between words
for i in words: #for  loop to interate between words
    print(i) #print command to present each line of words


############################################################################################################
#Example 

#user_sentence varibale will take input from user
#user_sentence will store string value
#input() builtin function has been udes
user_sentence = "My name is Hemant Thapa"
print()#spacing in line
words = user_sentence.split()#split() built in function has been used to split between words
for i in words: #for  loop to interate between words
    print(i) #print command to present each line of words