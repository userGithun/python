class bikeshop :
    
    def __init__(self,stock):
        self.stock = stock

    def showStock(self):
        print(f"Available bike rent {self.stock}") 

    def rentBike(self,qty):
        if (qty <= 0):
            print("Please enter positive number")
        elif (qty >= 0):
            print(f"Only {self.stock} bike's are available !")    
        else:    
            print(f"You want {qty} bike's for rent. Total price for {qty} bike , ${qty * 100}")  
            print(f"Remaining Bike's = {self.stock}")


dis = bikeshop(100)


while True:

    choose = int(input('''
                   1. Show Total bike\n
                   2. Bike For rent\n
                   3. Exit\n'''))
    
    if choose ==1:
        dis.showStock()
    elif choose ==2:
        qty=int(input("Enter the value for you need bike for rent :")) 
        dis.rentBike(qty)   
    elif choose ==3:
        print("\nThank youu for visiting Just2Bike\n")
        break
    else:
        print("INVALID INPUT, PLEASE TRY AGAIN!")


    



