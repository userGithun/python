# class bikeShop:
#     #stock = 100
#     def __init__(self,stock):
#         self.stock = stock
#         print(self.stock)

#     def displayBike(self):
#         print("Total Bikes",self.stock)
#     def rentForBike(self,q):
#         if q <= 0:
#             print("Enter the positive value or greater then zero")
#         elif q>self.stock:
#             print("enter the value (less the stock)")
#         else:
#             self.stock=self.stock-q 
#             print("Total Prices",q*100)
#             print("Total Bikes",self.stock)
# while True:
#     obj = bikeShop(100)
#     uc = int(input('''
# 1 Display stock
# 2 Rent a Bike
# 3 Exit                   
# '''))      
#     if uc ==1:
#         obj.displayBike()
#     elif uc ==2:
#         n = int(input("Enter qty"))
#         obj.rentForBike(n)  
#     else:
#         break               


## Simple Method

class BikeShop:
    def __init__(self, stock):
        self.stock = stock

    def show_stock(self):
        print(f"Available Bikes: {self.stock}")

    def rent_bike(self, qty):
        if qty <= 0:
            print("Please enter a positive number.")
        elif qty > self.stock:
            print(f"Only {self.stock} bikes are available.")
        else:
            self.stock -= qty
            print(f"You rented {qty} bike(s). Total cost: ₹{qty * 100}")
            print(f"Remaining Bikes: {self.stock}")


# Create the shop with an initial stock of 100 bikes
shop = BikeShop(100)

while True:
    choice = int(input('''\n1. Show Stock\n
    2. Rent a Bike\n
    3. Exit\n
    Choose an option: '''))

    if choice == 1:
        shop.show_stock()
    elif choice == 2:
        qty = int(input("Enter the number of bikes you want to rent: "))
        shop.rent_bike(qty)
    elif choice == 3:
        print("Thank you for visiting!")
        break
    else:
        print("Invalid option. Please try again.")


