                                                                       #PROGRAM 1

#pizza price
pizza={
    "margerita":199,
    "cheese paneer":399,
    "veg-veganza":259,
    "farmhouse":399,
    "kulhad pizza":159,

}
print("your pizza",pizza.keys())
#asking to user
b=input("choose pizza\n")
#show's the result
print("your pizza at just rupees:",pizza.get(b))


                                                                      #PROGRAM 2

#empty dict
contact ={}

#contact book
contact["police"]="100"
contact["ambulance"]="101"
contact["fire"]="1011"
contact["pankaj"] = "9340175399"
contact["harsh"] = "7806098369"
contact["pninfosys"] = "7000846823"
contact["rohit"] = "6866344646"
contact["ram"] = "75684683455"
contact["mohit"] = "6866344456"


#fn to pick up contact by name
def contact_num(name):
    if name in contact:
        print(f"{name}'s number is{contact[name]}")
    else:
        print(f"{name} is not in number.") 
# 
#ask to user
name_to_cont=input("Enter the name you want to contact:\n")  

#show's the result on display
print(contact_num(name_to_cont))

                                                                        #program3

# Creating a dictionary
person = {
    'name': 'John', 
    'age': 25, 
    'city': 'New York',
    }

# Checking if a key exists
if 'age' in person:
    print("Age is available:", person['age'])
else:
    print("Age is not available.")


                                                                        #program4

# Creating a dictionary
fruit_prices = {
    'apple': 250, 
    'banana': 40, 
    'orange': 150,
    }

# Asking user for the fruit name
fruit = input("Enter the name of the fruit (apple, banana, orange):\n ")

# Accessing the price of the fruit entered by the user
if fruit in fruit_prices:
    print(f"Price of {fruit} is: {fruit_prices[fruit]}")
else:
    print("Sorry, that fruit is not in the list.")

                                                                        #program 5

# Creating a dictionary
capitals = {'france': 'Paris', 'italy': 'Rome', 'japan': 'Tokyo'}

# Asking the user for the name of the country
country = input("Enter the name of a country (France, Italy, Japan):\n ")

# Checking if the country exists in the dictionary
if country in capitals:
    print(f"The capital of {country} is {capitals[country]}.")
else:
    print("Sorry, the capital of that country is not available.")


