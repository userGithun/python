class Employee:
    car = "pninfosys"
    ecode =120

class Freelancer:
    car = "google"
    level = 0


    def upgradeLevel(self):
        self.level = self.level + 1    

class Programmer(Freelancer,Employee):
    name = "vikas"


p = Programmer()
p.upgradeLevel()
print(p.level)
print(p.car)