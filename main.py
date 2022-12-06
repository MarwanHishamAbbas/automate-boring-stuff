# A shelf, is a persistent dictionary-like object. The beauty of it is that the values you save into a shelf can be any object you can pickle, so you're not restricted like you would be if you were using a database. Albeit interesting and useful, the shelve module is used quite rarely in practice. Just for completeness, let's see a quick example of how it works:

import shelve

class Person: 
    def __init__(self, name, id):
        self.name = name
        self.id = id
        


with shelve.open('shelf1.shelve') as db:
    db['obil1'] = Person('Marwan Hisham', 123)
    db['obil2'] = Person('Mohamed Hisham', 222)
    print(list(db.keys()))
