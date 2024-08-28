b = 12
x = 5

print(b > 3 and b < 10)
print(b > 3 or b < 4)
print(not(x > 3 and x < 10))

#step 2

username ="ram"
password =1234566

if(username == "ram" and password == '1234566')
    print("login")
else:
    print("username or password not match")    

#step 3

username ="ram"
password =1234566

if(username == "ram" or password == '1234566')
    print("login")
else:
    print("username or password not match")    

#step 4

username ="ram"
password =1234566

if( not (username == "ram" or password == '1234566'))
    print("login")
else:
    print("username or password not match")    

#step 5

username = int(input("enter name :"))
password = int(input("enter password:"))

if( username == "raju" and password == "123456")
    print("correct")
else:
    print("something went wrongh")    

