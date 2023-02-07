#List to store product name
product_name  = []
#List to store product price
product_price = []

#using foor loop to call input function 3 times
#for iterate in range (start, end, step):
for i in range(3):
    #input in string for product name
    #product1 = Coat, product2 = Pant, Product3 = Belt
    product =input("\nEnter product name: ")
    #input in float for product price
    #price1 = 55.50, price2 = 44.99, price3 = 20.89
    price = float(input("Enter price of your product: £ "))
    
    #Storing input() value in product_name 
    product_name.append(product)
    
    #Storing input() value in product price
    product_price.append(price)
    
#Storing value in different vaibale or segregation of price
price1 = product_price[0] #slicing for price2
price2 = product_price[1] #slicing for price2
price3 = product_price[2] #slicing for price3

product1 = product_name[0] #slicing for product name 1
product2 = product_name[1] #slicing for product name 1
product3 = product_name[2] #slicing for product name 1

total = sum(product_price)
average = (sum(product_price)/len(product_price))
print(f"\nAverage price of three products:{round(sum(product_price),2)}") #Math function sum() for caculating total of all value
print(f"Average price of three products: {round((sum(product_price)/len(product_price)),2)}") #Forging formula for mean vlaue

print(f"\n {product1} : £{price1}")
print(f" {product2} : £{price2}")
print(f" {product3} : £{price3}")

#Using f-string to representing values
print(f"\nThe Total of {product1}, {product2}, {product3} is {round(total,2)} and the average price of the items is {round(average,2)}")