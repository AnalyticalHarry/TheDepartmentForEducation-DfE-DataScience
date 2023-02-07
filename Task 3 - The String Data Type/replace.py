#storing string value "The!quick!brown!fox!jumps!over!the!lazy!dog!." in variable string1
string1 = "The!quick!brown!fox!jumps!over!the!lazy!dog!." 

#replacing "!" symbols with space " ", using replace() function and storing in string2 variable
string2 = string1.replace("!"," " )

#Changing string2 value into Capital letter with upper() function and storing in string3 variable 
string3 = string2.upper()

#Reversing the order of string3 value with  slice steps backwards and storing in string4 variable
string4 = string3[::-1]

print("\n",string2)
print("\n",string3)
print("\n",string4)