import math
#This print function will print message to user for selecting key words.
print("Investment - to caculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan\n")

#if user select "investment"then, it will take to invesment calculation
#if user select "bond" then, it will take to bond calculation
# "user_input" varibale will store string value into lower case, where lower() built-in function has been used
#lower() built-in in function has been used to convert all case into smaller
user_input = str(input("Please Enter \"Investment\" or \"Bond\": ").lower())

#"p" variable store numerical float value, p stand for principle amount or intial investment
if user_input == "investment":
    # "p" variable is applicable for investment
    p = float(input("Initial Principle balance you are depositing: £ "))
elif user_input == "bond":
    # "p2" varibale is applicable for bond
    p2 = float(input("Present value of the house: £ "))

#"r" & "i" are two different variable store same float value, i and r stand for rate of interest
r = i = float(input("Rate of interest (eg.if 7% is entered, then rate is 0.07): "))

#"t" & "n" are two different variable, which store same value or data types. it is for storing number of years
t = n = float(input("Number of years you have plan on investing (eg. if 10 year, then 10): "))

#if input of t or n is 1 than it should be year, but if user input greater than one than, it should be years.
#if t is equal to 1 then, y varible define year
if t ==1:
    #y variuable store string "year"
    y = "year"
elif t>=1:
    #y varibale store string "years"
    y = "years"
#########################################################################################################################
###################################################     INVESTMENT   ####################################################
#########################################################################################################################
#if user_input is equal to "investment", then it is True. which mean user enter string value matches.
#in second step, it will ask user to calculate simple interest or compound interest
if user_input == "investment":
    
    #if user want to calculate simple interest, they will type "simple"
    #if user want to calculate compound interest, they will type "compound"
    user_formula = str(input("Enter \"simple\" for Simple interest or \"compound\" for Compound Interest: ").lower())
    
    #if user input string, which will be store in "user_formula" variable matches with "simple", then it will be True
    #String comparision is sucessfull and True, it will run def fun() 
    if user_formula == "simple":
        
        #parameter are p, r, and t
        #p for principle, r for rate, and t for time
        def simple(p,r,t):
            
            #"simple_amount" varibale store formula for calculating final amount using simple interest formula
            simple_amount = p*(1+(r*t))
            
            #return will return simple_amount value
            return simple_amount
        
        #"result_simple" varibale store value from calling function
        result_simple = simple(p,r,t)
        
        #f-string has used to present valye
        #int(t) will project time
        #y will project, "year" or "years" which depends on value of "t" and "n"
        #math.ceil() has uesd to round up value
        print(f"\nFinal Amount after {int(t)} {y} with annual interest rate of {round((r*100),2)}% is £{round(result_simple, 2)}")
   
    #if user input string, which will be store in "user_formula" variable matches with "compound", then it will be True
    #String comparision is sucessfull and True, it will run def fun() 
    elif user_formula == "compound":
        
        #parameter are p, r, and t
        #p for principle, r for rate, and t for time
        def compound(p,r,t):
            
            #"compound_amount" varibale store formula for calculating final amount using compound interest formula
            compound_amount = p*((1+r)**t)
            
            #return will return compound_value
            return compound_amount
        
         #"result_compound" varibale store value from calling function
        result_compound = compound(p,r,t)
        
            #f-string has used to present valye
        #int(t) will project time
        #y will project, "year" or "years" which depends on value of "t" and "n"
        #math.ceil() has uesd to round up value
        print(f"\nFinal Amount after {int(t)} {y} with annual interest rate of {round((r*100),2)}% is £{round(result_compound,2)}")
#########################################################################################################################
###################################################       BOND     ######################################################
#########################################################################################################################
#if user_input matches to string "bond", then statment is true
elif user_input == "bond":
    #defining function has been used for creating bond formula
    #parameter are p, i and n. p stand for present value of house, i stand for annual interest rate, and n stand for years
    def bond_repayment(p2,i,n):
        i_monthly = i/12 #changing annual interest into montly interest
        n_monthly = n*12 #changing years into months
        x = (i_monthly*p2)/(1-(1+i_monthly)**(-n_monthly))
        return x
    montly_repayment = bond_repayment (p2,i,n)
    print(f"\nMonthly replayment amount is £{round(montly_repayment,2)}")