class Employee: 
    company="pninfosys"
    salary=100
    location = "delhi"

    def change(self):
        print(f"hello{self.location}")

    @classmethod
    def changeSalary(a, sal):
        a.salary = sal 
        print(f"hello{a.salary}")   


e = Employee()
# print(e.salary)
# e.change()        
e.changeSalary(5000)
print(e.salary)
print(Employee.salary)