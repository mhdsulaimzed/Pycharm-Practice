# class person:
#     def getdata(self):
#         self.id=int(input("enter the id"))
#         self.name=input("enter the nme")
#     def showdata(self):
#          print("id:"+str(self.id))
#          print("name:"+self.name)
# P1=person()
# P2=person()
# P1.getdata()
# P2.getdata()
# P1.showdata()
# P2.showdata()

#rectange
class rec:
    def __init__(self,l,b):
        self.leng=l
        self.bred=b
    def showdata(self):
        print("leangth:",self.leng)
        print("breadth:",self.bred)
    def area(self):
        a=self.leng*self.bred
        print("area",a)



R1=rec(5,6)
R2=rec(4,6)
R1.showdata()
R2.showdata()
R1.area()
R2.area()