#List comprehension with set range between 1 to 1000, for printing number from 1  to 1000
numbers = [x for x in range(1, 1000)]
print(f"\nNumber from 1 to 1000: {numbers}")#printing results

#List comprehension with set range between 1 to 1000,but if condition has used between 1 to 1000 only to print even number
even_numbers = [x for x in range(1,1000) if x % 2 == 0]
print(f"\nAll numbers in list are even: {even_numbers}")#printing result