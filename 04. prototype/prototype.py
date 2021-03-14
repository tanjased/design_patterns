import copy


class Address:
    def __init__(self, street_address, city, country):
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'

john = Person('John', Address('123 ndflb', 'Bogota', 'CU'))
print(john)


# Take a look at OOP course for instance references. How to create a copy
jane = copy.deepcopy(john)

# when we perform a shallow copy copy.copy(<instance>), the reference instance inside this instance will still refer to one object and can be overwritten
# while with a deep copy copy.deepcopy(<instance>) a completely independent object will be created.