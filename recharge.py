print("\nWelcome to BHARAT RECHARGE SERVICES\n")
num =int(input("Please Enter Your '10 Digit' Mobile Number :"))
balance =1000
if num == num:
    print("""Your Number is active\n
          Please Choose Your sim card carefully :\n
          1.Jio
          2.Airtel
          3.VI
          4.BSNL\n""")
sim=input("Please Choose Your sim card carefully :")
if sim=="jio" :
   print("""\nHere is your 'TOP 3' Jio Plan\n
         1.Rs.539 (Validity: 54 Days, 2.5GB/per )
         2.Rs.359 (Validity: 24 Days, 1.5GB/per )
         3.Rs.239 (Validity: 14 Days, 1.5/per with Unlimited 5G)\n""")
   plan=int(input("Please choose option btw ( 1, 2, 3 ):"))
   if plan == 1:
       print(f"""\nRecharge Details :\n
       MOBILE NUMBER :{num}
       NETWORK : JIO
       PLAN : Rs.539 (Validity: 54 Days, 2.5GB/per )\n""")
       pay = int(input(" Please Enter your amount :"))
       balance = balance- pay
       print(f"\nyou pay :{pay}")
       print(f"your updated balance is :{balance}\n")

       confirm=input("confirm recharge? (yes/no):")
       if confirm == "yes":
           print("\nRecharge successful!\n")
       else :
           print("\nRecharge canceled.\n")             
   elif plan == 2:
       print(f"""\nRecharge Details :\n
       MOBILE NUMBER :{num}
       NETWORK : JIO
       PLAN : Rs.359 (Validity: 24 Days, 1.5GB/per )\n""")

       pay = int(input(" Please Enter your amount :"))
       balance = balance- pay
       print(f"\nyou pay :{pay}")
       print(f"your updated balance is :{balance}\n")

       confirm=input("confirm recharge? (yes/no):")
       if confirm == "yes":
           print("\nRecharge successful!")
           print("THANK YOU FOR JOIN WITH US :)\n")
       else :
           print("\nRecharge canceled.")
           print("THANK YOU FOR JOIN WITH US :)\n")
    
   elif plan == 3:
       print(f"""\nRecharge Details : \n
       MOBILE NUMBER
       NETWORK  : JIO
       PLAN : Rs.239 (Validity: 14 Days, 1GB/per )\n""") 

       pay = int(input(" Please Enter your amount :"))
       balance = balance- pay
       print(f"\nyou pay :{pay}")
       print(f"your updated balance is :{balance}\n")

       confirm = input("confirm recharge? (yes/no):")
       if confirm == "yes":
           print("\nRecharge successful!")
           print("TAHNK YOU FOR JOIN WITH US :)\n")
       else :
           print("\nRecharge canceled.")
           print("THANK YOU FOR JOIN WITH US :)\n")


elif sim  == "airtel":
     print("""\nHere is your 'TOP 3' Airtel Plan\n
         1.Rs.599 (Validity: 28 Days, 2.5GB/per )
         2.Rs.399 (Validity: 14 Days, 1.5/per with Unlimited 5G)
         3.Rs.299 (Validity: 28 Days, 1GB/per )\n""")
         
         
     plan=int(input("Please choose option btw ( 1, 2, 3 ):"))
     if plan == 1:
       print(f"""\nRecharge Details :\n
       MOBILE NUMBER :{num}
       NETWORK : Airtel
       PLAN : Rs.599 (Validity: 28 Days, 2.5GB/per )\n""")

       pay = int(input("Please Enter your amount :"))
       balance = balance- pay
       print(f"\nyou pay :{pay}")
       print(f"your updated balance is :{balance}\n")

       confirm=input("confirm recharge? (yes/no):")
       if confirm == "yes":
           print("\nRecharge successful!")
           print("THANKS FOR JOINING US! :)")
       else :
           print("\nRecharge canceled.")
           print("THANKS FOR JOINING US! :)\n")
     elif plan == 2:
       print(f"""\nRecharge Details :\n
       MOBILE NUMBER :{num}
       NETWORK : Airtel
       PLAN : Rs.399 (Validity: 14 Days, 1.5/per with Unlimited 5G)\n""")

       pay = int(input("Please Enter your amount :"))
       balance = balance- pay
       print(f"\nyou pay :{pay}")
       print(f"your updated balance is :{balance}\n")

       confirm=input("confirm recharge? (yes/no):")
       if confirm == "yes":
           print("\nRecharge successful!")
           print("THANK YOU FOR JOIN WITH US :)\n")
       else :
           print("\nRecharge canceled.")
           print("THANK YOU FOR JOIN WITH US :)\n")  
     elif plan == 3:
       print(f"""\nRecharge Details : \n
       MOBILE NUMBER
       NETWORK  : Airtel
       PLAN : Rs.299 (Validity: 28 Days, 1GB/per )\n""")   

       pay = int(input("Please Enter your amount :"))
       balance = balance- pay
       print(f"\nyou pay :{pay}")
       print(f"your updated balance is :{balance}\n")

       confirm = input("confirm recharge? (yes/no):")
       if confirm == "yes":
           print("\nRecharge successful!")
           print("TAHNK YOU FOR JOIN WITH US :)\n")
       else :
           print("\nRecharge canceled.")
           print("THANK YOU FOR JOIN WITH US :)\n")            


elif sim  == "vi":
     print("""\nHere is your 'TOP 3' VI Plan\n
         1.Rs.499 (Validity: 28 Days, 2.5GB/per )
         2.Rs.359 (Validity: 14 Days, 1.5/per with Unlimited 5G)
         3.Rs.259 (Validity: 28 Days, 1GB/per )\n""")
         
         
     plan=int(input("Please choose option btw ( 1, 2, 3 ):"))
     if plan == 1:
       print(f"""\nRecharge Details :\n
       MOBILE NUMBER :{num}
       NETWORK : VI
       PLAN : Rs.499 (Validity: 28 Days, 2.5GB/per )\n""")

       pay = int(input("Please Enter your amount :"))
       balance = balance- pay
       print(f"\nyou pay :{pay}")
       print(f"your updated balance is :{balance}\n")

       confirm=input("confirm recharge? (yes/no):")
       if confirm == "yes":
           print("\nRecharge successful!")
           print("THANKS FOR JOINING US! :)\n")
       else :
           print("\nRecharge canceled.")
           print("THANKS FOR JOINING US! :)\n")
     elif plan == 2:
       print(f"""\nRecharge Details :\n
       MOBILE NUMBER :{num}
       NETWORK : VI
       PLAN : Rs.359 (Validity: 14 Days, 1.5/per with Unlimited 5G)\n""")

       pay = int(input("Please Enter your amount :"))
       balance = balance- pay
       print(f"\nyou pay :{pay}")
       print(f"your updated balance is :{balance}\n")
       confirm=input("confirm recharge? (yes/no):")
       if confirm == "yes":
           print("\nRecharge successful!")
           print("THANK YOU FOR JOIN WITH US :)\n")
       else :
           print("\nRecharge canceled.")
           print("THANK YOU FOR JOIN WITH US :)\n")  
     elif plan == 3:
       print(f"""\nRecharge Details : \n
       MOBILE NUMBER
       NETWORK  : VI
       PLAN : Rs.259 (Validity: 28 Days, 1GB/per )\n""") 
        
       pay = int(input("Please Enter your amount :"))
       balance = balance- pay
       print(f"\nyou pay :{pay}")
       print(f"your updated balance is :{balance}\n") 

       confirm = input("confirm recharge? (yes/no):")
       if confirm == "yes":
           print("\nRecharge successful!")
           print("TAHNK YOU FOR JOIN WITH US :)\n")
       else :
           print("\nRecharge canceled.")
           print("THANK YOU FOR JOIN WITH US :)\n")

elif sim  == "bsnl":
     print("""\nHere is your 'TOP 3' BSNL Plan\n
         1.Rs.499 (Validity: 28 Days, 2.5GB/per )
         2.Rs.249 (Validity: 14 Days, 1.5/per with Unlimited 5G)
         3.Rs.159 (Validity: 28 Days, 1GB/per )\n""")
         
         
     plan=int(input("Please choose option btw ( 1, 2, 3 ):"))
     if plan == 1:
       print(f"""\nRecharge Details :\n
       MOBILE NUMBER :{num}
       NETWORK : BSNL
       PLAN : Rs.499 (Validity: 28 Days, 2.5GB/per )\n""")

       pay = int(input("Please Enter your amount :"))
       balance = balance- pay
       print(f"\nyou pay :{pay}")
       print(f"your updated balance is :{balance}\n")

       confirm=input("confirm recharge? (yes/no):")
       if confirm == "yes":
           print("\nRecharge successful!\n")
       else :
           print("\nRecharge canceled.\n")
     elif plan == 2:
       print(f"""\nRecharge Details :\n
       MOBILE NUMBER :{num}
       NETWORK : BSNL
       PLAN : Rs.249 (Validity: 14 Days, 1.5/per with Unlimited 5G)\n""")

       pay = int(input("Please Enter your amount :"))
       balance = balance- pay
       print(f"\nyou pay :{pay}")
       print(f"your updated balance is :{balance}\n")
       confirm=input("confirm recharge? (yes/no):")
       if confirm == "yes":
           print("\nRecharge successful!")
           print("THANK YOU FOR JOIN WITH US :)\n")
       else :
           print("\nRecharge canceled.")
           print("THANK YOU FOR JOIN WITH US :)\n")  
     elif plan == 3:
       print(f"""\nRecharge Details : \n
       MOBILE NUMBER
       NETWORK  : BSNL
       PLAN : Rs.149 (Validity: 28 Days, 1GB/per )\n""") 
       
       pay = int(input("Please Enter your amount :"))
       balance = balance- pay
       print(f"\nyou pay :{pay}")
       print(f"your updated balance is :{balance}\n")

       confirm = input("confirm recharge? (yes/no):")
       if confirm == "yes":
           print("\nRecharge successful!")
           print("TAHNK YOU FOR JOIN WITH US :)\n")
       else :
           print("\nRecharge canceled.")
           print("THANK YOU FOR JOIN WITH US :)\n")