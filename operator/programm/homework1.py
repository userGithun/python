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

contact["ambulance"]="101"
contact["police"]="100"
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

#ask to user
name_to_cont=input("Enter the name you want to contact:\n")  

#show's the result on display
print(contact_num(name_to_cont))

