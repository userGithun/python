                                                         #program1

# # Meal suggestion based on time of day

time_of_day = "evening"

if time_of_day == "morning":
    print("Time for breakfast!")
elif time_of_day == "afternoon":
    print("How about some lunch?")
elif time_of_day == "evening":
    print("Dinner time!")
else:
    print("Grab a snack!")

                                                          #program2

# Simple number comparison

number = 15

if number > 20:
    print("The number is greater than 20.")
elif number == 20:
    print("The number is exactly 20.")
else:
    print("The number is less than 20.")

                                                          #program3

# Simple traffic light simulator

light_color = "red"

if light_color == "green":
    print("Go!")
elif light_color == "yellow":
    print("Slow down!")
elif light_color == "red":
    print("Stop!")
else:
    print("Invalid light color.")


                                                           #program 4

# Simple grade checker

grade = 85

if grade >= 90:
    print("You got an A!")
elif grade >= 80:
    print("You got a B!")
elif grade >= 70:
    print("You got a C!")
elif grade >= 60:
    print("You got a D!")
else:
    print("You got an F!")

                                                           #program 5

# Simple season finder based on month

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

                                                            #program 6    

#asking to user
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))
num4 = int(input("Enter Number 4: "))
 
#finding greatest value 
if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"{num1} is greatest")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(f"{num2} is greatest")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print(f"{num3} is greatest")
else:
    print(f"{num4} is greatest")


                                                            #program 7    

num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


                                                              #program 8

# Get the user's age
age = int(input("Enter your age: "))

# Determine the ticket price based on age
if age < 5:
    print("The ticket is free for children under 5.")
elif age >= 5 and age <= 12:
    print("The ticket price is $5 for children aged 5 to 12.")
elif age >= 13 and age <= 17:
    print("The ticket price is $7 for teenagers aged 13 to 17.")
elif age >= 18 and age <= 59:
    print("The ticket price is $10 for adults aged 18 to 59.")
else:
    print("The ticket price is $6 for seniors aged 60 and above.")


                                                                #program 9

print("welcome to INOX PVR cinema")
print("1.Stree 2\n 2.Border 2\n.3 Deadpool\n ")
movie = int(input("select your show:\n"))

if movie=="stree2":
    print("Timeing 9:30PM AUDI 2")
elif movie=="border 2":
    print("timing 8:00pm AUDI 1")
elif movie=="deadpool":
    print("timing 7:30pm AUDI 3")
else:
    print("please try again")    

