class papa:
    company = "pninfosys"

    def showdetails(self):
        print("this is an emplayee")



class son(papa):
    language= "python"
    #company = "google"

    def getLanguage(self):
        print(f"The language is {self.language}")
        # def showDetails(self):
        #     print("this is an Programmer")


# e = papa()
# e.showdetails()     
p = son()
p.showdetails()
print(p.company)   
