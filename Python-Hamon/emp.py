import logging


logging.basicConfig(filename='emp.log',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')




class Example():
    def __init__(self,first,last):
        self.fname=first
        self.lname=last

        logging.info(f"hello {self.fullname}")
    @property 
    def fullname(self):
        fullname = self.fname + self.lname
        return fullname
    

a =Example("allen","kumman")
