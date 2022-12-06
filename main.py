import pickle
from dataclasses import dataclass

@dataclass
class Person:
    first_name:str
    last_name: str
    id: int

    def greet(self):
        print(f"Hi, I'm {self.first_name} {self.last_name} ID: {self.id}")


people = [Person('Marwan', 'Hisham', 124), Person('Mohamed', 'Hisham', 333)]

# save data in binary format to a file
with open('data.pickle', 'wb') as stream:
    pickle.dump(people, stream)

# load the data from the file 
with open('data.pickle', 'rb') as stream:
    peeps = pickle.load(stream)


for person in peeps:
    person.greet()