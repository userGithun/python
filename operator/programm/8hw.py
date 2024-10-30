#1 program 
for i in range(1, 6):
    print(i)

#2 program
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

#3 program
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

#4 program
for i in range(1, 11):
    if i == 5:
     break
    print(i)

#5 program
for i in range(1,11):
   if i==5:
      continue
   print(i)

#6 program pass
for i in range(5):
    if i == 3:
        pass  # Do nothing when i is 3
    else:
        print(i)

#7 program pass
x = 10
if x > 5:
    pass  # Do nothing if x > 5
else:
    print("x is less than or equal to 5")

#8 program pass
status = "pending"

if status == "completed":
    print("Task is completed.")
elif status == "pending":
    pass  # Task is still pending, no action needed right now
else:
    print("Task status is unknown.")

#9 program pass
count = 0

while count < 5:
    pass  # Keep looping until count is less than 5
    count += 1

print("Count reached 5.")

# 10 program pass
try:
    number = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    pass  # Ignore the error

print("No action taken on ZeroDivisionError.")


