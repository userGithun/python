# num=int(input("enter the number for multiplication table :"))
# i= 1
# while i <=10:
    # print(f"{num} x {i} = {num * i}")
    # i += 1    
# 
# 
# while True:
    # square=input("for 'square' to type square or 'exit' to stop:")
# 
    # if square=="exit":
        # break
# 
# if square =="sqaure": 
# 
    # digit=int(input("Enter the number for square :"))
    # a = digit*digit
    # print("square="(a))



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
