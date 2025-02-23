#try Except Exception Handling

num1 = input("Enter the number 1:\n")
num2 = input("Enter the number 2:\n")
try:
    print("The sum of these two numbers is",int(num1)+int(num2))
except Exception as e:
    print(e)    

print("pninfosys gwalior")



##### 2

num1 = input("Enter the number 1:\n")
num2 = input("Enter the number 2:\n")
try:
    print("The sum of these two numbers is",int(num1)+int(num2))
except Exception as e:
    print(e)    

print(int(num1)+int(num2))