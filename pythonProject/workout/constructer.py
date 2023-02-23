class Mysample:
    year = 2022

    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place

    def display(self):
        print(Mysample.year)
        print("name:", self.name)
        print("age:", self.age)
        print("place:", self.place)

    def add_age(self):
        # mysample.year=mysample.year+1
        self.age = self.age + 1

    def relocate(self, place):
        self.place = place

    @classmethod
    def addyear(cls):
        cls.year = cls.year + 1
    # @staticmethod
    def display_welcome(self):
        print("Welcome motherfckers")

P = Mysample("sulaim", 22, "kakkad")
P.display_welcome()
P.display()
P.add_age()
P.relocate("mattanur")
# P.addyear()
Mysample.addyear()
print("--------------------------------------------------")
P.display()
P.display_welcome()