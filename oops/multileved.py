class person :
    conuntrt = "india"


    def takeBreath(self):
        print('Gwalior')

class Employee(person):
    company ="home"


    def getSalary(self):
        print("salary 10000")
    def takeBreath(self):
       super().takeBreath()
       print("pninfosys")


class Programmer(Employee):
    company = "Fiverr"


    def getSalary(self):
        print(f"no salary to programmers")

    def takeBreath(self):
        super().takeBreath()   
        print("I am an Programmer so I am Luckily breathing++...")     

p = Programmer()
p.takeBreath()                   
# e = Employee()
# e.takeBreath()
# pr = person()
# pr.takeBreath()