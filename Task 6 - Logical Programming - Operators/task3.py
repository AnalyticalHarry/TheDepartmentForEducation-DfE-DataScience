#User input for swiming time, cycling time, and running time
#float()  buil-in function is used in input and input() built-in function has been used
swiming =  float(input("Enter swiming time: "))
cycling = float(input("Enter cycling time: "))
running = float(input("Enter running time: "))


#total of triathlon activity
#"user_time" variable store total value from addition operation of swiming, cycling and running
user_time = swiming+cycling+running


#print time taken for completing individual task
print("\nTime taken for swiming", swiming)
print("Time taken for cycling", cycling)
print("Time taken for running", running)
print(f"\nTotal time taken:{user_time}")

#if statement for comparing between "user_time" variable which is overall activity to "time" varibale
#if player user_time is equal to time, than statement is true and print "Provincial Colours"
if user_time <= 100:
    print("\nProvincial Colours")
    
#elif statement for comapring "user_time" variable and 5 minutes of qualifying time
#print will be "Half Provincial Colours"
elif (user_time > 100 and user_time <=105):
    print("\nProvincial Half Colours")
    
#elif statement for comapring "user_time" variable and 10 minutes of qualifying time
#print will be "Half Provincial Scroll"
elif (user_time >105 and user_time <=110):
    print("\nProvincial Scroll")
    
#elif statement for comapring "user_time" variable is greater than "time" varibale
#print will be "No award"
elif user_time>110:
    print("\nNo award")
    