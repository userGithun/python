# e = 20
# while e < 30:
#     print("yes" + str(e))
#     e = e +1
# else:
#     print("good job")    

for var1 in range(1,6):
    for var2 in range(1,6):
        if(var1%var2!=0):
            pass
        elif(var2<var1):
            continue
        else:
            print(var1*var2) 