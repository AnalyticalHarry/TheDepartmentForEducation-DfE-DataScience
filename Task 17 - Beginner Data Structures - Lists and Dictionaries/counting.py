#defining a function counting
def counting(sample_string):
    #converting string into list
    sample_string_list = list(sample_string)
    #using dictonary casting
    counts = dict()
    #Create a for loop to iterate through sample_string_list
    for i in sample_string_list:
        #counting each string value 
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    #returning count of each string value
    return counts
#printing result on screen
print("Expected Result:",counting("google.com"))