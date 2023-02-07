#declaring function "days_of_weeks"
def days_of_week():
    
    #declaring list of all the days of the week
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    #Creating for loop to interate in list
    for day in days:
        print(day)
#calling function
days_of_week()


sample_sentence = "My name is hemant thapa and learning functions in python"
#Defining function "replace_second_word" 
def replace_second_word(sentence):
    
    # spliting sentence into words
    words = sentence.split()

    #Creating for loop itering in words
    for i in range(len(words)):
        
        # If the current word is the second word in the list, replace it with "hello"
        if i % 2 == 1:
            words[i] = "hello"

   #Join back sentence
    modified_sentence = " ".join(words)

    # Returning value 
    return modified_sentence

#assiging call function into variable
modified_sentence = replace_second_word(sample_sentence)

#printing result
print(modified_sentence)
