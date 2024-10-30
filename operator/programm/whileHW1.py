                         #program 1

count = 5
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")
# 
                         #program 2

user_input = ""             #Yah line ek khali string h,shuruaat mein mein kuch nahi hota.
while user_input != "exit": #Jab tak value "exit" ke barabar nahi ho jati,tab tak yeh loop chalti rahegi.
    user_input = input("Type 'exit' to stop the program: ") #user"exit" likhkr enter karega,tab loop ruk jygi
print("Program stopped.")

                         #program 3

while True:             #True matlab yeh hai ki yeh loop tab tak chalta rahega jab tak usse manually roka na jaaye.
    user_input = input("Type 'exit' to stop: ")
    if user_input == "exit":
        break           #break ka kaam hai loop ko turant rok dena. Matlab, yah loop yahin khatam ho jayega
print("Program terminated.")

                         #program 4

password = "python123"
user_input = ""

while user_input != password:
    user_input = input("Enter the password: ")

print("Access granted!")

                         #program 5


num = int(input("Enter a number for multiplication table: "))
i = 1

while i <= 10:      # i ki value 10 se chhoti ya barabar honi chaiye.
    print(f"{num} x {i} = {num * i}")
    i += 1          #Jaise jaise loop chalta rahega,i badhta jaayega,or table ka agla result print hota jaayega.

                         #program 6

while True:  #Yeh line ek infinite loop banata hai
             # Loop tab tak chalta rahega jab tak hum ise manually break statement se nahi rokte.
    operation = input("Enter operation (+, -, *, /) or 'exit' to stop: ")
    
    if operation == "exit":
        break

    if operation in ['+', '-', '*', '/']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == '+':
            print(f"Result: {num1 + num2}")
        elif operation == '-':
            print(f"Result: {num1 - num2}")
        elif operation == '*':
            print(f"Result: {num1 * num2}")
        elif operation == '/':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Division by zero!")
    else:
        print("Invalid operation! Please enter +, -, *, or /.")
