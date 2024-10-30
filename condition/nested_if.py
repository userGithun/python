# x = 180
# 
# if x > 20:
    # print("above 15,")
    # if x < 2:
        # print("and also above 25!")
    # else:
        # print("but not above 20.") 
# else:
    # print("no")           
# 
# Program to perform basic arithmetic operations

operator = input("Enter operator ( + , - , * , / ):")

#ask to user
num1 = int(input("Enter the first value :"))
num2 = int(input("Enter the second value :"))

#perform the operator

if operator=="+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator=="-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator=="*":
    print(f"{num1} * {num2} = {num1 * num2}")   
elif operator=="/":
    if num2==0:
        print("Error: divisible by zero is not allowed")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")  
else:
    print("invalid request: please try one of + , - , * , / :")          