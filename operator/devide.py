a = int(input("enter number 1:"))
b = int(input("enter number 2:"))

c = a+b
print("addition", c)

#division

a = int(input("enter number 1:"))
b = int(input("enter number 2:"))

c =(a/b)
print ("division", c)

#remaider

a = int(input("enter the number:"))
b = int(input("enter the number:"))

print("the remainder is",a%b)

#average

a = int(input("enter the number:"))
b = int(input("enter the number:"))

avg = (a+b)/2
print("the average is",avg)

#square

a = int(input("enter number "))

c = (a*a)
print("square",c)

#perform all program

a = int(input("enter number:"))
b = int(input("enter number:"))

c = ("addition", a+b,
      "subtract", a-b, 
      "multiplication", a * b,
      "division", a/b)
print(c)