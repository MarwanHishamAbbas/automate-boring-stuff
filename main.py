class Student: 
    no_of_students = 0
    def __init__(self, name, age, courses):
        self.__name = name
        self.__age = age
        self.__courses = courses
        Student.no_of_students += 1
    
    def display(self):
        print(f"My name is {self.__name}, I'm {self.__age} years old and I'm studing {self.__courses[1]} ")




student_1 = Student('Marwan Hisham', 23, ['Math', 'Science'])

student_1.display()