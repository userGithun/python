print("Welcome to CBI BANK Gwalior")
restart="y"
chance=3
balance=120000

while chance >=0:
    pin= int(input("Please enter your four digit password :"))
    if pin==(1769):
        print("you have enter the next lebel\n")
        while restart not in ("n" "No" "no" "N"):
            print("Press 1 to Balance Enquiry\n ")
            print("Press 2 Cash Withdraw\n")
            print("Press 3 to balance pay in\n")
            print("Press 4 to balance Return card\n")
            option = int(input("what should you like to choose number:"))
            if option == 1:
                print("Your balance is Rs.",balance,"\n")
                restart=input("would you like to go back:")
                if restart in("n" "No" "no" "N"):
                    print("Thank you for banking with CBI BANK")
                    break
            elif option == 2:
                    withdraw=int(input("how much you want to withdraw amount,\n rs.100/rs.200/rs.500/rs.2000/rs.5000:"))
                    if withdraw*[100,200,500,2000,5000]:
                        balance = balance-withdraw
                        print("\n Your last amount is now Rs.",balance)
                        restart = input("\n would you like to do (restart=yes Otherwise= no)")
                        if restart in ("n" "no" "No" "N"):
                            print("Thank you for banking with CBI BANK")
                            break
                        elif withdraw !=[100,200,500,2000,5000]:
                            print("INVALID amount \n Please re-try")
            elif option == 3:
                    payin = float (input("Please enter your Amount :"))
                    balance= balance+ payin 
                    print("\nYour total balance is now Rs.",balance)
                    restart= input("would you like to do (restart=yes Otherwise= no)")
                    if restart in ("n" "N" "no" "No"):
                        print("Thank you for Banking with CBI BANK")
                        break
            elif option ==4:
                        print("Okey please wait your card is returned.......................")
                        restart="y"
            else:
                print("Please enter Correct Numbers:")
    elif pin !=(1769):
        print("You have enterned wrong password")
        chance = chance-1
        if chance == 0:
            print("\n no more tries, please contact support@pninfosys.com")            
                              


