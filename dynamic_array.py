class People:
    def __init__(self, name:str, age:int, gender:str) -> None:
        """means nothing is returned in the constructer"""
        self.nationality = "Lebanese"
        self.name = name
        self.age = age
        self.gender = gender

    def printer(self)-> None: # printer constrcuter does not return anything 
        print(self.nationality, self.name, self.age, self.gender) 

    def calculate_year(self, year)-> int:
        new_age = year - self.age

        return new_age


person1 = People("Ramez", 21, "male")
person2 = People("Tiana", 22, "female")

person1.printer()
person2.printer()
print(person1.calculate_year(2025))
print(person2.calculate_year(2024))