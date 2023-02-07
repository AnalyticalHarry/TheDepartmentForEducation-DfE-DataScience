#************* HELP *****************
# If you are having any difficulties, please feel free to contact our specialist team on Discord for support.
# The best way to get help is to login to Discord at https://discord.com/invite/hyperdev where our specialist team is ready to support you.
#************************************

# ========= User-Defined Functions  ===========


# ========= How to Define a Function ===========
# Defining a function simply means creating a function.
# You begin with the keyword def followed by the name of the function and parentheses, ().
# You place any input parameters (values passed to the function) within these parentheses.
# You then place a colon (:) after the parenthese to signify the start of the indented code block.
# The indented code block contains statements that provide the functionality to your function.
# The last statement in the indented code block is the return statement.
# This statement exits the function and can also pass a value back to the caller.

# The general syntax of a function in Python is as follows:
# def function_name(parameters):
#       statements
#       return (expression)


# ************ Example 1 ************

def add_one(x):
    y = x + 1
    return y

# Explanation:
# This function is called 'add_one', it takes as input the parameter 'x'.
# We can call the input variable (here x) anything we want.
# It's just a name we give it so we know how to refer to it within the function (every indented line under the def add_one(x) line is 'within' the function).
# The code indented under 'def add_one' is the logic of the function. It defines what happens when the function is called.
# Simply put, the function computes a new variable y, which is the value stored in variable x with 1 added to it.
# It then 'returns' the value y.


# ========= Calling a Function ===========
# In order to execute a function, you need to 'call' it.
# You call a function by using the functions name followed by the values you would like to pass into it within parentheses.

# ************ Example 2 ************
# If you 'called' the function we previously defined with the value of x = 10, it would look exactly like this:

print("Example 2: ")
num = 10
print("10 plus 1 is equal to: " + str(add_one(num)) + ".")
# This will call the function add_one defined above and pass the integer 10 to it.
# The function will then return 11 and it will be printed out.

# ************ Example 3 ************
# You can also call a function and store the value returned by it in a variable.

print("\nExample 3: ")
num = add_one(4)
print("4 plus 1 is equal to: " + str(num) + ".")


# Think of the 'call to the function', i.e. add_one(num) , as a 'placeholder' for some computation.
# The function will go off and run its code, and return its result in that place.


# ========= Function Parameters ===========
# In the function definition, you put the names of variables that you what to store the input values to, between the parentheses after the function name.
# You can put more than one of these variables or parameters, simply separate them by commas.

# ************ Example 4 ************
print("\nExample 4: ")
def power(base, exponent):
    result = base ** exponent
    return (result)


print(power(3, 5))

# Here we've created a function which accepts two arguments and returns the result of the base to the power exponent using the ** operation (where x ** y means x^y).
# Note the order of the values in the calling statement.
# 3 is passed to the variable base while 5 is passed to the variable exponent.


# ************ Example 4 ************
def double_this_number(number):
        y = number * 2 # Multiples the number by 2.
        return y


# ************ Example 5 ************
def return_first_letter_word(word):
        y = word[0]
        return y

# ************ Example 6 ************
def put_number_in_list(num):
        newList = []
        newList.append(num)
        return newList

# ************ Example 7 ************
def put_number_in_list_if_big(num):
        newList = []
        if num >100:
                newList.append(num)
        return newList # Be careful! This could return an empty list.

# ************ Example 8 ************
def compute_sum_of_two_numbers(num1, num2):
        y = num1+num2
        return y

# ************ Example 9 ************
def takes_no_parameters():
        y = "This function takes no parameters as input, but that means its functionality is limited...."
        return


# As you can see from the examples above, you can pretty much do anything you want in a function.
# You can create new data structures, use conditionals etc.
# We can call the input variable anything we want. It's just a name we give it so we know how to refer to it within the function.
# As seen in the second to last example, we can have multiple input parameters too. There's no limit on them, as long as you can keep track of what's what!
# In the last example, we have a function that takes no input parameters. This is also possible, but it means the user who calls the function has limited interaction with the function - they can't supply any input!
# In the case of some functions - imagine a function that returned the current time i.e. - getTime() - it makes sense to see why they need no input parameters (unless you had a more complex function like get_time(timezone) which returned the time for a specific timezone the calling user provides!)
# Values passed into the function through the 'function's parameters' (variables e.g. num1 and num2 above) will be referenced with those variable names.
# Think of it as copying in the values from the inputted parameter values when 'calling' the function to these 'function parameters'.


# While the above functions may not seem useful, this is because they are so simple. You can have functions with hundreds of lines that do complex tasks.
# However it is often very useful to define functions that do one specific task with a few lines of codes as opposed to a complicated function that does many tasks with hundreds of lines of code.
# i.e. break up a complicated function into many simpler functions so that it is easier to understand the function's role and find errors!




# =========== Functions Without Return Statements ===========
# Functions do not need to have a return statement

# ************ Example 10 ************
print("\nExample 10:")
def print_word(word):
        print(word)


# The function above just prints out something, it doesn't have a return statement.
# That's okay, but it means that if you make a call like:

y  = print_word("abc")


# y will store the special value None.
# This is not a String or any other data type, so it will cause an error when trying to do other things with it.
# Be careful that your functions return values, if that's what you need them to do.


# ************ Example 11 ************
print("\nExample 11:")
# We can call the function multiple times in a loop:

num = 10
for i in range(10):
    num = add_one(num)  #Runs 10 times, each time, 1 is added to the value of 10. So after the first iteration it will be 11, the second iteration computes 11 + 1 = 12, etc... until 20.

print(num)




# =========== Scope ===========
# Scope is what we call a program’s ability to find and use variables in a program. The rule of thumb is that a function is covered in one-way glass: it can see out, but no one can see in.
# This means that a function can call variables that are outside the function, but the rest of the code cannot call variables that are defined within the function.

# *********** Example 12 ****************
print("\nExample 12:")
j = 5

def do_something():
    # Output -> 5
    print(j)

do_something()

# Output -> 5
print(j)

# The above function can see outside and so fetches j from outside the function. Let's see what happens when this goes wrong.

# *********** Example 13 ****************
print("\nExample 13:")
j = 5

def do_something():
    j = 7
    # Output -> 7
    print(j)

do_something()

# Output -> 5
# j = 7 made a *new* local variable x in do_something
# it didn't change the outer j
print(j)

# Here, we assigned a value to the global variable j inside the function, which then created a new local variable. That is why j inside the function equals 7,
# but j outside the function equals 5.


# ======================= Play around with Python a bit ============================
#
#   Create a new Python file in this folder called funcpractice.py.
#   Inside it, create a function called 'add_three', that takes as input three parameters -- num1, num2, num3.
#   Then, write logic to create a new variable, y, that is the sum of all three of these numbers.
#   Then, return the result y.
#   Now, after you've defined this function, write a function call to return the sum of the numbers 52, 25, and 1403.
#   Store this result in a variable called sum_func.
#   Print out sum_func. Don't forget to cast to a string!
#
# ==================================================================================================



# ****************** END OF EXAMPLE CODE ********************* #