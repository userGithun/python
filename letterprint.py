letter='''\nDear <|NAME|>,
You are selected!
have a greate day ahead!
pninfosys <|NAME|>

Date: <|DATE|>

'''
name = input("Enter Your Name\n")
date = input("Enter Date\n")

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>",date)

print(letter)

# name = input("Enter your name:")
# p = input("Enter your Physics marks:")
# c = input("Enter your chemistry marks:")
# m = input("Enter your maths marks:")

# marksheet= '''Name: <|NAME|>

#    Marksheet
# -----------------
# Physics   | <|p|>
# Chemistry | <|c|> 
# maths     | <|m|>
#  '''

# marksheet = marksheet.replace("<|p|>",p)
# marksheet = marksheet.replace("<|c|>",c)
# marksheet = marksheet.replace("<|m|>",m)
# marksheet = marksheet.replace("<|NAME|>",name)

# print(marksheet)


#practice

# name = input("Enter your name :")
# p = input("Enter your physics marks :")
# c = input("Enter your chemistry marks :")
# m = input("Enter your maths marks :")
# b = input("Enter your biology marks :")


# sheet = """
#         Name : <|NAME|>


#         Marksheet     
# --------------------------

#     Physics   :  <|p|>
#     Chemistry :  <|c|>
#     Maths     :  <|m|>
#     Biology   :  <|b|>

# """
# sheet = sheet.replace("<|NAME|>",name)
# sheet = sheet.replace("<|p|>",p)
# sheet = sheet.replace("<|c|>",c)
# sheet = sheet.replace("<|m|>",m)
# sheet = sheet.replace("<|b|>",b)

# print(sheet)