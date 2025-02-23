# Simple Fibonacci Program

num = int(input("Enter the number of terms: "))

a, b = 0, 1

if num <= 0:
    print("Please enter a positive number.")
elif num == 1:
    print(f"Fibonacci sequence: {a}")
else:
    print("Fibonacci sequence:")
    for i in range(num):
        print(i)
        print(a, end=" ")
        a, b = b, a + b
