# # Mobile Recharge Program

# def mobile_recharge():
#     # Get user input
#     mobile_number = input("Enter your mobile number (10 digits): ")
#     if len(mobile_number) != 10 or not mobile_number.isdigit():
#         print("Invalid mobile number. Please enter a 10-digit number.")
#         return
    
#     try:
#         amount = float(input("Enter recharge amount: "))
#         if amount <= 0:
#             print("Invalid amount. Please enter a positive number.")
#             return
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
#         return

#     # Operator selection
#     print("\nSelect your operator:")
#     print("1. Airtel")
#     print("2. Jio")
#     print("3. Vi")
#     print("4. BSNL")
#     operator_choice = input("Enter the number of your operator: ")
    
#     operators = {"1": "Airtel", "2": "Jio", "3": "Vi", "4": "BSNL"}
#     operator = operators.get(operator_choice)

#     if not operator:
#         print("Invalid operator selection.")
#         return
    
#     # Confirmation
#     print("\nRecharge Details:")
#     print(f"Mobile Number: {mobile_number}")
#     print(f"Operator: {operator}")
#     print(f"Amount: ₹{amount}")
    
#     confirm = input("Confirm recharge? (yes/no): ").strip().lower()
    
#     if confirm == 'yes':
#         print("Recharge successful!")
#     else:
#         print("Recharge canceled.")

# # Run the program
# mobile_recharge()


#######rough

# print("Welcome to VI app")
# login = "plans"
# chance = 3
# DTHRecharge = "view your plan"
# Balance =  100000 
# if chance >= 0 :
#      pin = int(input("Please enter your registered mobile number:\n"))
#      if pin == 9200727816 :
#           print("Login Succesfull" + " enter what you choose")
#           login = ("would you like to back")
#           while login  not in ("no" "NO" "n" "No" "N"):
#                print("option 1 = Mobile recharge ")
#                print("option 2 = DTH recharge")
#                print("option 3 = Check Balance")
#                option = int(input("Choose option between (1,2,3):\n"))
#                if option == 1:
#                     print(" ")
#                     p = int(input("enter the mobile number"))
#                     num = {
#                          "            "
#                     }
#                     print("Choose a plan")
#                     print("Rs.200 , Rs.500 , Rs.600")
#                     plan = int(input("enter a plan"))
#                     plan = [ 200,500,600]
#                     if plan == 200:
#                          print([num]+200,"valid for 28 days / 1.5GB /day")



#######rough

print("\nWelcome to BHARAT RECHARGE SERVICES\n")
num =int(input("Please Enter Your '10 Digit' Mobile Number :"))
if num == num:
    print("""Your Number is active\n
          Please Choose Your sim card carefully :\n
          1.Jio
          2.Airtel
          3.VI
          4.BSNL\n""")
sim=input("Please Choose Your sim card carefully :")
if sim=="jio":
   print("""\nHere is your 'TOP 3' Jio Plan\n
         1.Rs.239 (Validity: 24 Days, 1.5GB/per )
         2.Rs.359 (Validity: 14 Days, 1.5/per with Unlimited 5G)\n""")
   plan=int(input("Please choose option btw ( 1, 2, 3 ):"))
   if plan == 1:
       print(f"""\nRecharge Details :\n
       MOBILE NUMBER :{num}
       NETWORK : JIO
       PLAN : Rs.239 (Validity: 24 Days, 1.5GB/per)\n""")
       confirm=input("confirm recharge? (yes/no):")
       if confirm == "yes":
           print("\nRecharge successful!\n")
       else :
           print("\nRecharge canceled.\n") 
    
           
       
   elif plan == 2:
       print(f"""\nRecharge Details :\n
       MOBILE NUMBER :{num}
       NETWORK : JIO
       PLAN : Rs.359 (Validity: 14 Days, 1.5/per with Unlimited 5G)\n""")
       confirm=input("confirm recharge? (yes/no):")
       if confirm == "yes":
           print("\nRecharge successful!")
           print("THANK YOU FOR JOIN WITH US :)\n")
       else :
           print("\nRecharge canceled.")
           print("THANK YOU FOR JOIN WITH US :)\n")
else:
    print("INVALID INPUT,PLEASE TRY AGAIN! ")   