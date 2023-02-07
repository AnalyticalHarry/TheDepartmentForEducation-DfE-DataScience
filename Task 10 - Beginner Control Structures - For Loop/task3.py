row = 5 #numer of row for "*" has been declared
# outer loop
for i in range(1, row + 1):
    # inner loop
    for j in range(1, i + 1):
        print("*", end="")#printing "*" and end="" for making space in print
    print('')#spacing between each itreated value