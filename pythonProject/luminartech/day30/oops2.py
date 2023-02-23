class Students:
    def readdata(self):
        self.n=input("enter the name")
        self.r=int(input("enter the roll number"))
    def displaydata(self):
        print("name:",self.n)
        print("Roll:",self.r)


class Grade(Students):
    def readdata(self):
        super().readdata()
        self.totalmark=int(input("entee the total mark"))
    def calgrade(self):
       p = self.totalmark/500*100
       if p >= 80:
           print("A grade")
       elif p >= 60:
           print("B grade")
       elif p>=40:
           print(" C grade")
       else:
           print("failed grade")

obj1=Grade()
obj1.readdata()
obj1.displaydata()
obj1.calgrade()


