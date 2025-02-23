# def demo():
#     print("hello")
#     demo()
# demo()    
#1000

# n = int(input("Enter the value of n:"))

# def natural(n):
#     if n==0:
#         return
#     print(n)
#     return natural(n-1)
# natural(n)


# def num(n):
#     if (n<=0):
#         return
#     print(n,end="")
#     num(n-1)

# def num1(n):
#     print(n,end="")
#     num(n-1) 
# num1(10)     



def factorial(num):
    if num ==1 or num==0:
        return num
    return num*factorial(num-1) 

number = int(input("Enter a number:"))
result = factorial(number)
print("Factorial of",result)



