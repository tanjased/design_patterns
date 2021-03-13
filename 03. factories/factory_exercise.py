import itertools


class Person:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'Person: {self.id}: {self.name}'

class PersonFactory:
    id = itertools.count()

    def create_person(self, name):
        p = Person(next(PersonFactory.id), name)
        return p

p1 = PersonFactory.create_person('y','Celine')
p2 = PersonFactory.create_person(0,'Celine')
print(p1,'\n',p2)
