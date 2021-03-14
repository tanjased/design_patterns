import copy


class Address:
    def __init__(self, street_address, suite, city):
        self.suite = suite
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f'{self.street_address}, Suite #{self.suite}, {self.city}'


class Employee:
    def __init__(self, name, address):
        self.address = address
        self.name = name

    def __str__(self):
        return f'{self.name} works at {self.address}'

# instead of making copies manually, we make prototype factory
# we have 2 office categories
class EmployeeFactory:
    main_office_employee = Employee("", Address("123A East Dr", 0, "London"))
    aux_office_employee = Employee("", Address("123B East Dr", 0, "London"))

    # adding a copy of a new employee
    @staticmethod
    def __new_employee(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    # and here the employee office classification itself
    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee,
            name, suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name, suite
        )


# main_office_employee = Employee("", Address("123 East Dr", 0, "London"))
# aux_office_employee = Employee("", Address("123B East Dr", 0, "London"))

# john = copy.deepcopy(main_office_employee)
# john.name = "John"
# john.address.suite = 101
# print(john)

# would prefer to write just one line of code
jane = EmployeeFactory.new_aux_office_employee("Jane", 200)
print(jane)


#### So if you have a fixed number of prototypes in your code, it's better to put them
# into a factory and then create a bunch of factory methods, so the construction of copies of those
# prototypes is easier.