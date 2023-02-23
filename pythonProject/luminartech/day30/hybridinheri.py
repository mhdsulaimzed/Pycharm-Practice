class Student:
    def readdata(self):
        self.name=input("enter the name")
        self.roll=int(input("enter the roll number"))
    def displaydata(self):
        print("name:",self.name)
        print("roll:",self.roll)
class Test(Student):
    def readmark(self):
        self.total=int(input("enter the total mark"))
    def displaymark(self):
        print("total mark:",self.total)

class Grade(Test):
   def calgrde(self):
       p=self.total/100
       if p >= 80:
           print("A grade")
       elif p >= 60:
           print("B grade")
       elif p >= 40:
           print(" C grade")
       else:
           print("failed ")
obj1=Grade()
obj1.readdata()
obj1.displaydata()
obj1.readmark()
obj1.displaymark()
obj1.calgrde()