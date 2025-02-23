l =[10,20,30,40]
print(len(l))    #len function
s = "welcome"
print(len(s))

#overloading
# class pn:
#     def displayinfo(self,name=''):
#         print("welcome to pninfosys"+name)

# obj = pn()
# obj.displayinfo()
# obj.displayinfo('mits')  #function 


#overriding
# class pn():
#     def displayinfo(self):
#         print("welcome to pninfosys")
# class itm(pn):
#     def displayinfo(self):
#         print("welcome to pninfosys123")        

# obj = itm()
# obj.displayinfo()

#overloading

# class area:
#     def find_area(self,x=None,y=None):
#         if x != None and y != None:
#             print(x*y)
#         elif x != None:
#             print(x*x)
#         else:
#             print('nothing') 

# obj1=area()
# obj1.find_area()
# obj1.find_area(10)
# obj1.find_area(10,20)         #function same but 3 kam ek rah hai


#overriding
class A :
    def showData(self):
        print("im in A class")
class B(A):
    def showData(self):
        super().showData() 
        print('i m in B class')  

obj = B()
obj.showData()             