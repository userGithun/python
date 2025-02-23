class Employee:
    company="Google"

    def itm(self,a):
        print(f"Hello,{self.company} ITM Gwalior{a}")

    @staticmethod
    def rjit(a):
        # print(f"Hello,{self.company} ITM Gwalior{a}")
        print(a)    



rohit=Employee()
rohit.itm("delhi")
rohit.rjit("ram")
