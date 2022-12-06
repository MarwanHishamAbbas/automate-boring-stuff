# Polymorphism.py
class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name is {self.name} and age is {self.age} "

class Man(Person):
    gender = 'Male'
    no_of_men = 0
    def __init__(self, name,age,voice):
        super().__init__(name, age)
        self.voice = voice
        Man.no_of_men += 1


    def display(self):
        # overwrite the display method
        string = super().display()
        return string + f"and have {self.voice} and gender is {self.gender}"

person1 = Man('Marwan Hisham', 23, 'Deep voice')
person2 = Man('Mohamed Hisham', 25, 'Deep voice')

print(person1.display())
print(Man.no_of_men)