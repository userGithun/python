print("Please select your delicious pizza.")
print("1.Margerita")
print("2.Farmhouse")
print("3.Veg.vegenza")

choose_pizza =(input("select the pizza according to your mood:"))
if choose_pizza ==1.:
    choose ="Margerita"
elif choose_pizza==2:
    choose="Farmhouse"
elif choose_pizza==3:
    choose="Veg.vegenza"

else:
    choose= None

if choose_pizza:
    print(f"you have choose a {choose_pizza} pizza")
    print("please select your pizza size")
    print("1.regular")
    print("2.medium")
    print("3.large")
pizza_size=(input("enter the size of pizza"))
if pizza_size==1:
     size="regular"
elif pizza_size==2:
    size="medium"
elif pizza_size==3:
    size="large"
else:
    size=None

if pizza_size:
   print=(input(f"you have choosen a {pizza_size} pizza"))
   print("please choose the toppings")
   print("1.Onion")
   print("2.Tomato")
   print("3.garlic")
 
choose_toppings=(input("enter the toppings"))
if choose_toppings==1:
    toppings="Onion"
elif choose_toppings==2:
    toppings="garlic"
elif choose_toppings==3:
    toppings="Extra cheese" 
else:
    toppings=None

if toppings:
    print(f"you have order a {choose_pizza} pizza with {pizza_size} add on {choose_toppings} toppings")
else:
    print("invalid pizza choice & size and toppings also, please recreate your order and try again.")