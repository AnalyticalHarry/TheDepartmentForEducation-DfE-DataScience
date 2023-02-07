import matplotlib.pyplot as plt 
import numpy as np 
import csv  

#open csv file 
outfile = open("piechartdata.csv","r")  

#let the program know it is a csv 
file = csv.reader(outfile)  

#skip the header ('letter','value') 
next(file, None)  

#create arrays to store the values 
category = [] 
value = []  

#iterates through the file
for row in file:     
     category.append(row[0]) #appends 'letter' into category       
     value.append(row[1]) #appends 'value' into value  

#appends the array values into pie chart 
plt.pie(value, labels=category)  

#show
plt.show()
