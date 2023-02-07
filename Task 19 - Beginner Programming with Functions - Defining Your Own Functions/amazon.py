# Define the functions for minimum value
def min_val(numbers):
    min_val = min(numbers)
    return f"The min of {numbers} is {min_val}."

#Defining the function for maximum value
def max_val(numbers):
    max_val = max(numbers)
    return f"The max of {numbers} is {max_val}."


def avg_val(numbers):
    avg_val = sum(numbers) / len(numbers)
    return f"The avg of {numbers} is {avg_val:.1f}."

#Defining function operation
def operation(line):
  # Split the line 
    parts = line.split(':')
    operation = parts[0]
    numbers = list(map(int, parts[1].split(',')))

  #returing value for operation
    if operation == "min":
        return min_val(numbers)
    elif operation == "max":
        return max_val(numbers)
    elif operation == "avg":
        return avg_val(numbers)

# Read the text file
with open("input.txt", "r") as file1:
      lines = file1.readlines()

#storing result in list
results = []
for i in lines:
    result = operation(i)
    results.append(result)

# Write the results to text file
with open("output.txt", "w") as file2:
      for j in results:
        file2.write(j + "\n")
        
#printing result on screen
print(results[0])
print(results[1])
print(results[2])
