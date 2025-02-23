# class student:
#     __name = "ravi" #private variable direct object ke sath use nahi hota hai...


#     def __init__(self): #constructor ki help se call kr skte h..
#         print(self.__name)
#         self.__displayinfo()


#     def __displayinfo(self): #PRIVATE
#         print("hello gwalior")    

#     def itm(self):
#         self.__displayinfo()
#         print(self.__name)

# obj = student()
# #print(obj.__name)
# obj.itm()            



#Encapsulation getter and setter

class students:
    def __init__(self):
        self._name = ""

    def getname(self):
        return self._name
    
    def setname(self,name):
        self._name= name

obj = students()
obj.setname('raj')
name = obj.getname()
print(name)        
