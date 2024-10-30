# for i in range(5):
#     print("*" *(i+1))
#     # print("*" * (i))

   #2

# n =3
# for i in range(3):
#     print(" " * (n-i-1), end="")
#     print("*" * (2*i+1), end="")
#     print(" " * (n-i-1)) 

   #3

# n =4
# for i in range(5):
#     print((n-i) * " " + i* '*')

   #4

# n = 5
# for i in range (0,n):
#     for j in range(0,i+1):
#         print("*" , end=" ")
#     print()   
# 

   #5

# n = 5                            
# for j in range(1,n+1):
#     print("*" * j) 

   #6

n = 5
for i in range(n + 1 , 0, -1):
    for j in range(0, i - 1):
        print("*" , end=" ")
    print(" ")    

   #7

# n =6
# for n in range(1, n):

#     num =1

#     for j in range(n,0 , -1):

#         if j > n:

#             print(" ", end=" ")

#         else:

#             print("*", end=" ")

#             num = num +1

#     print("")            

    
  # 8 same as 7

# n = 6
# for i in range(1, n):
    
#     for j in range(i, 0, -1):
#         print("*", end=" ")
#     print("")

