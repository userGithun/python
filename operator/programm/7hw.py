#1          program to print from n to 1 while loop


# Get input from use
# n = int(input("Enter a number: "))

# # Initialize a variable
# i = 1

# # While loop to print from 1 to n
# while i <= n:
#     print(i)
#     i += 1


#2          program to print from n to 1 while loop


# Get input from user
# n = int(input("Enter a number: "))

# # Initialize the variable to n
# i = n

# # While loop to print from n to 1
# while i >= 1:
#     print(i)
#     i -= 1


#3          program to find sum from 1 to n while loop


# Input: The value of n
n = int(input("Enter a number f: "))

# Initialize sum and counter
total_sum = 0
i = 1

# While loop to calculate the sum
while i <= n:
    total_sum += i
    i += 1

# Output: The sum from 1 to n
print(f"The sum of numbers from 1 to {n} is: {total_sum}")


#4           program to print sum of square from 1 to n while loop


# Input: The value of n
n = int(input("Enter a number: "))

# Initialize sum and counter
sum_of_squares = 0
i = 1

# While loop to calculate the sum of squares
while i <= n:
    sum_of_squares = sum_of_squares + i*i
    i += 1

# Output: The sum of squares from 1 to n
print(f"The sum of squares from 1 to {n} is: {sum_of_squares}")


#5           program to print sum of cube from 1 to n while loop


# Input: The value of n
n = int(input("Enter a number: "))

# Initialize sum and counter
sum_of_cubes = 0
i = 1

# While loop to calculate the sum of cubes
while i <= n:
    sum_of_cubes += i*i*i
    i += 1

# Output: The sum of cubes from 1 to n
print(f"The sum of cubes from 1 to {n} is: {sum_of_cubes}")


#6             program to print only even numbers between 1 to n while loop

# Input: The value of n
n = int(input("Enter a number: "))

# Initialize counter
i = 2  # Start from 2, as it's the first even number

# While loop to print even numbers
while i <= n:
    print(i)
    i += 2  # Increment by 2 to get the next even number


#7              program to print only odd numbers between 1 to n while loop


# Input: The value of n
n = int(input("Enter enter number :"))

# Initialize counter
i = 1  # Start from 1, as it's the first even number

# While loop to print even numbers
while i<=n:
    print(i)
    i += 2    # Increment by 2 to get the next odd number


 #8             program to find some of digits of a given number simple to understand


    # Input: The value of the number
num = int(input("Enter a number: "))

# Initialize sum to 0
sum_of_digits = 0

# While loop to calculate the sum of digits
while num > 0:
    digit = num % 10        # Get the last digit of the number
    sum_of_digits += digit  # Add the digit to the sum
    num = num // 10         # Remove the last digit from the number

# Output: The sum of digits
print(f"The sum of the digits is: {sum_of_digits}")


#9 program

# Creating a dictionary
person = {
    'name': 'John', 
    'age': 25, 
    'city': 'New York',
    }

# Checking if a key exists
if 'age' in person:
    print("Age is available:", person['age'])
else:
    print("Age is not available.")


 #10 program

month =input("Enter your favorite month:\n")

if month in ["december", "january", "february"]:
    print("It's Winter!")
elif month in ["march", "april", "may"]:
    print("It's Spring!")
elif month in ["june", "july", "august"]:
    print("It's Summer!")
elif month in ["september", "october", "november"]:
    print("It's Fall!")
else:
    print("Invalid month.")