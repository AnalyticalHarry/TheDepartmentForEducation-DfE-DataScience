#input string value and save in variable product1
#product1 = "Shirt"
product1 =input("Enter first product name: ")

# a = 24.99
#float() built-in function types for product one price
a =float(input("Enter price of first product £: "))

#input string value and save in variable product2
#product2 = "Shoes"
product2 =input("\nEnter second product name: ")

#float() built-in function types for product two price
#b = 119.99
b =float(input("Enter price of second product £: "))

#input string value and save in variable product3
#product3 = "Jacket"
product3 =input("\nEnter third product name: ")

#float() built-in function types for product three price
#c = 84.99
c =float(input("Enter price of your third product £: "))

#feeding a,b,c float value in defining function()  
def shopping(a,b,c):
    a,b,c = a,b,c
    return a,b,c
result = shopping (a,b,c)

#change into data type to list
product = [result]

#storing value to value from silicing method
price1 = product[0][0]
price2 = product[0][1]
price3 = product[0][2]

#sum of all price
total = price1+price2+price3

#average of price
#using tupple cuz of immutable properties
average = (price1+price2+price3)/3

print("\nTotal of all three products:", round(total,2),)
print("Average price of three products:", round(average, 2),)
print(f"\n {product1} : £{price1}")
print(f" {product2} : £{price2}")
print(f" {product3} : £{price3}")
#Using f-string to representing values
print(f"\nThe Total of {product1}, {product2}, {product3} is {round(total,2)} and the average price of the items is {round(average,2)}")