#defining function for hotel cost
def hotel_cost(nights):
    #formula for calculating nights
    price_per_night = nights*120
    #returning value
    return price_per_night

#defining function for plane cost
def plane_cost(city):
    #list of city in west
    west = ["glasgow","london", "paris","rome","lisbon","amsterdam","athens","madrid","barcelona"]
    if city in west:
        #price of flight
        price = 200
        #returning price value
        return price
    
    #list of city in middle east 
    middle = ["dubai", "amadiya", "petra", "doha", "beirut", "baalbek", "manama"]
    if city in middle:
        #price for flight
        price = 500
        #returning price value
        return price
    
    #list of city in south east
    south_east = ["tokyo", "jakarta","bangkok","hanoi","singapore","manila","bali"]
    if city in south_east:
        #price of flight
        price = 800
        #returning price value
        return price
    
    else:
        #price of flight
        price = 700
        #returning price value
        return price

#Defining function for car rental
def car_rental(num_days):
    #car rent formula
    car_rent = num_days * 100 #£100 per day
    #returning car rent value
    return car_rent

#user input in days
nights = int(input("Enter number of nights:  "))
#user input city name
city = str(input("Enter the name city: "))
#user input car rent days
num_days = int(input("Enter number of days to rent car: "))

#list for storing all values
total_expenses = []
#define function holidays and taking three arguments
def holidays(nights, city, num_days):
    #hotel price
    hotel_price = hotel_cost(nights)
    #plane price
    plane_price = plane_cost(city)
    #car rental price
    car_rental_price  = car_rental(num_days)
    
    #appending all values into list "total_expenses"
    total_expenses.append(hotel_price)
    total_expenses.append(plane_price)
    total_expenses.append(car_rental_price)
    
    #print output result
    print(f"\nPrice of hotel {hotel_price}")
    print(f"Price of plane {plane_price}")
    print(f"Price of car rental {car_rental_price}")

holidays(nights, city, num_days)

print(f"\nTotal Expenses for travelling is {sum(total_expenses)}")