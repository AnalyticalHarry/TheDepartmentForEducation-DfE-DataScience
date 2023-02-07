import matplotlib.pyplot as plt
import numpy as np

#Prepare the data
x = np.linspace(0, 100, 100) #x axis
y = np.sin(x) # y values

#Plot the data
plt.plot(x, y, label="sine")

#Create a title
plt.title("My first matplotlib sine graph")

#Show the plot
plt.show()
