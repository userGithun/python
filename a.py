# a = input("enter number")


# print(a)

# a =10
# b =10

# if(a==b):
#     print("yes")
# else:
#     print("no")    


# age = int(input("enter your age 1:"))
# 
# if(age>=18):
    # print("you are alegible")
# else:
    # print("you're not alegible")    
# 

print("Welcome to the delicious pizza.")
print("please choose the siz of pizza.")
print("1. Small")
print("2. Medium")
print("3. Large")

size_choice = int(input("enter the size number of pizza"))
if size_choice == 1:
    size = "small"
elif size_choice == 2:
    size = "medium" 
elif size_choice == 3:
    size = "large"
else:
    size = None   

if size_choice:
    print(f"you have chosen a {size_choice}pizza") 
    print("please choose the toppings")
    print("1. olives")
    print("2. mushrooms")        
    print("3. extra cheese")

    toppings_choice = int(input("enter the of topping"))
    if toppings_choice == 1:
        topping = "olives"
    elif toppings_choice == 2:
        topping = "mushroom"
    elif toppings_choice == 3:
        topping = "extra cheese"
    else:
        topping = None    

if topping:
    print(f"you have ordered a {size_choice} pizza with {toppings_choice} toppings.")
else:
    print("invalid pizza size and topping choice. please restart the order and try again.")