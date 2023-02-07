##Variable storing fundamental values

#Price for  air service per kilometer
air = 0.36 #R0.36 per km

#price for sea service per kilometer
freight = 0.25 #R0.25 per km

#price for full inusrance cover
full_insurance = 50 #R50.00

#price for Limited insurance cover
limited_insurance = 25 #R25.00

#price for gift
gift = 15 #R15

#zero for no gift
no_gift = 0 #R0

#price for priority delivery
priority_delivery  = 100 #R100

#price for standard delivery
standard_delivery = 20 #R20


#x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x--x-x--x-x-x-x-x--x-x--x-x-x
#User will input distance in kilometer
#float() built-in function has been used for storing float value in "user_distance" variable
user_distance = float(input("Enter total distance of the delivery in kms: "))

#print command has been used to provide  details on postage of mail
print("\n Would you like  an Air Mail or Sea Mail")

#transport varibale will store string value data types from user
#"air" or "sea" in small letter are important to type for selecting airmail or seamail
#if user type "air" than control flow operation will navigate to if statement or user input "sea" than it will navigated to elif statement
transport = str(input("Type --> \"air\" or \"sea\": "))
################################################################################################################################ 
##############################                        "Airmail"                       ##########################################
################################################################################################################################
#Airmail
#if statement will compare input string value entered by user, which are stored inside varibale named "transport"
if transport == "air":
#Transport_price varibale store the summation of distance enter by user and airmail price per kilometer
    transport_price = user_distance*air
    #round() built-in has been used to round up by two decimal  place
    print("\nAirmail price:R",round(transport_price,2))
    
###############################################################################################################################
#Asking user for insurance 
#Type "full" for full insurance or Type "limited" for limited insurance
    print("\nWould you like to cover full insured or limited insurance?")
    #insurance varibale store string input which are "full" or "limited"
    #user are only allowed to enter "full" or "limited"
    #if user enter "full" than if statement will work
    #if user eneter  "limited" than elif statement will work
    insurance = str(input(f"\n Type -> \"full\"  or  \"limited\": "))
    if insurance == "full":
#if string value type is full, then full insurance will be sum of transport price and full insurance 
        full_insurance = transport_price + full_insurance
        #round() built-in function has been used to present vatriable "full_insurance" value into neareast two decimal place
        print("\nPrice of Airmail plus Full insurance:R",round(full_insurance,2))
        print("\nWould  you like to gift or no gift?")
        
#Asking user for  adding gift or no gift
#if they want gift type "yes" or if they don't want gift type "no"
        user_gift = str(input("Type -> \"yes\" for gift or \"no\" for no gift: "))
        if user_gift == "yes":
        #gift variable store total of transport price, gift price and full insurance price
            gift = gift + full_insurance 
            print("\nPrice of Airmail, Full insurance and Gift:R", round(gift, 2))
            print("\nWould you Priority service or Standard service?")
            
#Asking user for adding priority delivery or standard service
#Type "p" for priority service and "s" for standard service
            user_service = str(input("Type -> \"p\" or \"s\""))
            if user_service == "p":
            #priority_delivery store total of transport price, gift price and full insurance price, and priority_delivery price
                priority_delivery = priority_delivery + full_insurance 
                print("Price of Airmail, Full insurance, Gift, and Priority delivery:R", priority_delivery)
            elif user_service =="s":
            #standard_delivery store total of transport price, gift price and full insurance price, and standard_delivery price
                standard_delivery  = standard_delivery + full_insurance 
                print("Price of Airmail, Full insurance, Gift, and Standard_delivery ",standard_delivery )
        else:
            #no_gift varibale store full_insurance value
            no_gift = no_gift + full_insurance
            print("\nNo Gift :", round(no_gift,2))
            
#Asking user for adding priority delivery or standard service
#Type "p" for priority service and "s" for standard service
            user_service = str(input("Type -> \"p\" or \"s\""))
            if user_service == "p":
                #priority delivery variblestore addition of priority delivery and no gift,no gift is zero
                priority_delivery = priority_delivery + no_gift
                print("Price of Airmail, Full insurance, Gift, and Priority delivery:R", priority_delivery)
            elif user_service =="s":
                #standard_delivery store total of transport price, no gift price and full insurance price, and standard_delivery price
                standard_delivery  = standard_delivery + no_gift
                print("Price of Airmail, Full insurance, Gift, and Standard_delivery ",standard_delivery )
            

###############################################################################################################################          
    elif insurance == "limited":
        limited_insurance = transport_price + limited_insurance
        print("\nPrice of Airmail plus limited insurance:R",round(limited_insurance,2))
        print("\nWould  you like to gift or no gift?")
        
#Asking user for  adding gift or no gift
#if want gift type "yes" or "no" for no gift
        user_gift = str(input("Type -> yes for gift or no for no gift: "))
        if user_gift == "yes":
            gift = gift + limited_insurance 
            print("\nPrice of Airmail, Full insurance and Gift:R", round(gift, 2))
            print("\nWould you Priority service or Standard service?")
            
#Asking user for adding priority delivery or standard service
#Type "p" for priority service and "s" for standard service
            user_service = str(input("Type -> p or s"))
            if user_service == "p":
                #priority delivery = total cost of transport price, gift, limited insurance and priority postage
                priority_delivery = priority_delivery + gift
                print("Price of Airmail, Full insurance, Gift, and Priority delivery:R", priority_delivery)
            elif user_service =="s":
                #standard_delivery store total of transport price, gift price and limited insurance price, and standard_delivery price
                standard_delivery  = standard_delivery + gift
                print("Price of Airmail, Full insurance, Gift, and Standard_delivery ",standard_delivery )
        else:
            no_gift = no_gift + limited_insurance
            print("\nNo Gift :", round(no_gift,2))
            
#Asking user for adding priority delivery or standard service
#Type "p" for priority service and "s" for standard service
            user_service = str(input("Type -> p or s"))
            if user_service == "p":
            #priority_delivery variable store total cost of transportation, limited insurance, priority_delivery, and no_gift
                priority_delivery = priority_delivery + no_gift
                print("Price of Airmail, Full insurance, Gift, and Priority delivery:R", priority_delivery)
            elif user_service =="s":
            #standard_delivery variable store total cost of transportation, limited insurance, priority_delivery, and no_gift
                standard_delivery  = standard_delivery + no_gift 
                print("Price of Airmail, Full insurance, Gift, and Standard_delivery ",standard_delivery )
               
        
        
################################################################################################################################ 
##############################                        "Freight"                       ##########################################
################################################################################################################################
elif transport == "sea":
    transport_price = user_distance*freight
    print("\nFreight price: R",transport_price)
    
###############################################################################################################################
#Asking user for insurance 
#Type "full" for full insurance or Type "limited" for limited insurance

    print(f"\nWould you like to Full insured or limited insurance?")
    #insurance varibale store string input which are "full" or "limited"
    #user are only allowed to enter "full" or "limited"
    #if user enter "full" than if statement will work
    #if user eneter  "limited" than elif statement will work
    insurance = str(input("\nType -> \"full\"  or  \"limited\": "))
    
#if string value type is full, then full insurance will be sum of transport price and full insurance 
    if insurance == "full":
        full_insurance = transport_price + full_insurance
        print("\nPrice of Freight plus Full insurance:R",round(full_insurance,2))
        print("\nWould  you like to gift or no gift?")
        
#Asking user for  adding gift or no gift
#if want gift type "yes" or "no" for no gift
        user_gift = str(input("Type -> \"yes\" for gift or \"no\" for no gift: "))
        if user_gift == "yes":
            gift = gift + full_insurance 
            print("\nPrice of Freight, Full insurance and Gift:R", round(gift, 2))
            print("\nWould you Priority service or Standard service?")
            
#Asking user for adding priority delivery or standard service
#Type "p" for priority service and "s" for standard service
            user_service = str(input("Type -> \"p\"or \"s\""))
            if user_service == "p":
                priority_delivery = priority_delivery + gift 
                print("Price of Freight, Full insurance, Gift, and Priority delivery:R", priority_delivery)
            elif user_service =="s":
                standard_delivery  = standard_delivery + gift 
                print("Price of Freight, Full insurance, Gift, and Standard_delivery ",standard_delivery )
        else:
            no_gift = no_gift + full_insurance
            print("\nNo Gift :", round(no_gift,2))
            
#Asking user for adding priority delivery or standard service
#Type "p" for priority service and "s" for standard service
            user_service = str(input("Type -> \"p\" or \"s\""))
            if user_service == "p":
                priority_delivery = priority_delivery + no_gift
                print("Price of Airmail, Full insurance, Gift, and Priority delivery:R", priority_delivery)
            elif user_service =="s":
                #standard_delivery store total of transport price, gift price and full insurance price, and standard_delivery price
                standard_delivery  = standard_delivery + no_gift
                print("Price of Airmail, Full insurance, Gift, and Standard_delivery ",standard_delivery )
  
            
###############################################################################################################################          
    elif insurance == "limited":
        limited_insurance = transport_price + limited_insurance
        print("\nPrice of Freight plus limited insurance:R",round(limited_insurance,2))
        print("\nWould  you like to gift or no gift?")
        
#Asking user for  adding gift or no gift
#if want gift type "yes" or "no" for no gift
        user_gift = str(input("Type -> \"yes\" for gift or \"no\" for no gift: "))
        if user_gift == "yes":
            gift = gift + limited_insurance 
            print("\nPrice of Freight, Full insurance and Gift:R", round(gift, 2))
            print("\nWould you Priority service or Standard service?")
            
#Asking user for adding priority delivery or standard service
#Type "p" for priority service and "s" for standard service
            user_service = str(input("Type -> \"p\" or \"s\""))
            if user_service == "p":
                priority_delivery = priority_delivery + gift
                print("Price of Freight, Full insurance, Gift, and Priority delivery:R", priority_delivery)
            elif user_service =="s":
                #standard_delivery store total of transport price, gift price and full insurance price, and standard_delivery price
                standard_delivery  = standard_delivery + gift
                print("Price of Freight, Full insurance, Gift, and Standard_delivery ",standard_delivery )
        else:
            no_gift = no_gift + limited_insurance
            print("\nNo Gift :", round(no_gift,2))
            
#Asking user for adding priority delivery or standard service
#Type "p" for priority service and "s" for standard service
            user_service = str(input("Type -> \"p\" or \"s\""))
            if user_service == "p":
            #priority_delivery variable store total cost of transportation, limited insurance, priority_delivery, and no_gift
                priority_delivery = priority_delivery + no_gift 
                print("Price of Freight, Full insurance, Gift, and Priority delivery:R", priority_delivery)
            elif user_service =="s":
                #standard_delivery store total of transport price, gift price and full insurance price, and standard_delivery price
                standard_delivery  = standard_delivery + no_gift
                print("Price of Freight, Full insurance, Gift, and Standard_delivery ",standard_delivery )
               
        
        