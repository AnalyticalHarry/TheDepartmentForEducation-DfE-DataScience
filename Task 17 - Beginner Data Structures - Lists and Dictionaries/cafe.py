#menu contains list of cafe items
menu = ['drink', 'Sandwich', 'cake', 'crips']
#stock contains quantity of items
stock = {'drink':100, 'Sandwich':50, 'cake':30, 'crips':500}
#individual price of an items
price = {'drink':1.49, 'Sandwich':2.99, 'cake':1.99, 'crips':0.65}

#declared total_quantity zero
total_quantity = 0
#Create a for loop to iterate through menu
for i in menu:
    #total quantity will be sum of all indivdual itmes price multilplying by total number of individual stock
    total_quantity += price[i] * stock[i] 
#printing result
print("The total stock worth in cafe is £" + (str(total_quantity)))