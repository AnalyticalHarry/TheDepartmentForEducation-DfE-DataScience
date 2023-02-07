#This is a bunch of words
str_manip = input("Enter a sentence: ") #Str_manip variable has store input() of string "This is a bunch of words" 

length_of_string = len(str_manip) #len() is used to calculate length of string
print("\nLength of string: ",length_of_string,"\n")

str_manip_2 = str_manip.replace("s", "@") #replace() function is used to replace "s" with "@"
print("S replaced by @: ", str_manip_2)

string_manip_index = str_manip[-3:] #slice is used to get last three letter "rds"
string_manip_index2 = string_manip_index[::-1] #reversing of string "rds" to "sdr"
print("\n3 characters in str_manip backwards: ",string_manip_index2) 

string_manip_index3 = str_manip[0:3] #slice is used again to get first three letters of string "Thi"
string_manip_index4 = str_manip[-2:] #slice of string "ds" which is last two characters in str_manip
string_concatenation = str(string_manip_index3 + string_manip_index4) #Concatenation of two string and using str() function
print("\nfive-letter word that is made up of the first three and the last two characters: ",string_concatenation )