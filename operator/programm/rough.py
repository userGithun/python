# i = 3
# while i<5:
#     j=1
#     while j<5:
#         print(j, end="")
#         j = j + 1
#     k = 2
#     while k<5:
#         print(k,end="")
#         k = k + 1
#     l = 2
#     while l<5:
#         print(l,end="")
#         l = l+1
#     i = i +1

# i =1
# while i<=5:
#     j=1
#     while j<=i:
#         print(" ", end=" ")
#         j=j+1
#     k = 1  
#     while k<=i:
#         print("*",end=" ")  
#         k=k+1 
#     print() 
#     i = i+1  

# n =5
# i =1
# while (n>0):
#     b=1
#     while (b<i):
#         print(" ", end="")
#         b= b+1
#     j = 1
#     while (j<=(n*2)-1):
#         print("*",end="")   
#         j=j+1 
#     print()
#     n= n-1
#     i= i+1    

 #tcs question 1

# n = 10
# user = int(input("Enter quantity :"))

# c = (n-user)
# print(f"number of sold candies =",user)
# print(f"Number of candies available in a jar =", c)

#example 2

# n = 10
# user = int(input("Enter candies quatity :"))

# if user in range(1,6):
#     print("number of sold candies =",user)
#     print("number of candies available =",n-user)
# else:
#     print("Invalid Input")
#     print("number of candies left =",n)    

#example 2.1     

# weight = int(input("Enter clothes weight :"))

# if weight == 2000:
#     print("estimate time is 25 minutes")
# elif weight == (2001 and 4000):
#     print("estimate time is 35 minutes")
# elif weight == 4000:
#     print("estimate time is 45 minutes")
# elif weight== 0:
#     print("time taken is 0")   
# elif weight== 7000:
#     print(" weight is overload")     
# else:
#     print("Invalid")       

#example 2.2

# a = int(input("Enter the weight of clothes in gram "))
# if (a==0):
#     print("time taken is 0 minute")
# elif (a<=2000):
#     print("time taken is 20 minute")
# elif (a <=4000):
#     print("time taken is 35 minutes")
# else:
#     print("time taken 45 minute")            


#example 2.3

n = int(input())
if n==0:
    print("Time Estimate : 0 Minutes")
elif n in range(1,2001):
    print("Time Estimate : 25 Minutes")    
elif n in range(2001,4001):
    print("Time Estimate : 35 Minutes")    
elif n in range(4001,7001):
    print("Time Estimate : 45 Minutes")  
else:
    print("Invalid Input")      
