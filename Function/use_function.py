#No Argument No Return

# def add():
#     a = int(input("Enter 1st No:"))
#     b = int(input("Enter 2nd No:"))
#     c = a+b
#     print("sum =",c)
# add()    


#with Argument No Return
# def add(a,b):
#     c= a + b
#     print("Addition =",c)

# a = int(input("Enter 1st No:"))
# b = int(input("Enter 2nd No:"))
# add(a,b) #value pass


#No Argument with return
# def add():
#     a = int(input("Enter 1st No:"))
#     b = int(input("Enter 2nd No:"))
#     c = a + b
#     return c

# s = add()
# print("Addiction =",s)


#With Argument with return
# def add(a,b):
#     c= a + b
#     return c

# a = int(input("Enter 1st No:"))
# b = int(input("Enter 2st NO:"))
# x = add(a,b)
# print("Addiction =",x)


#Greatest value

def maximum(n1,n2,n3):
    if ( n1 > n2):
        if (n1>n3):
            return n1
        else:
            return n3
    else :
        if(n2>n3):
            return n2
        else:
            return n3

n1 = int(input("Enter 1st No:"))
n2 = int(input("Enter 2nd No:"))
n3 = int(input("Enter 3rd No:"))
m = maximum(n1,n2,n3)
print("The value of the maximum is "+ str (m))   
# 
    
    