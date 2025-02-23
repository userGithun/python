no = int(input("Enter the no till what you want the series"))
a =0 
b =1
c =0
i =1

while (i<no):
    c=a+b
    a=b
    b=c
    i = i +1
    print(c)
    print("The febonacci sequence for the given no "+str(no)+"is:",c)