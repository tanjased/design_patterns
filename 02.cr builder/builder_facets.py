# How can you get several builders participating in a build-up of an object?
# How can you make a nice looking interface where you can switch between builders?

class Person:
    def __init__(self):
        print('Creating an instance of Person')
        # address
        self.street_address = None
        self.postcode = None
        self.city = None
        # employment info
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return f'Address: {self.street_address}, {self.postcode}, {self.city}\n' + \
               f'Employed at {self.company_name} as a {self.postcode} earning {self.annual_income}'


# We want to have 2 separate builders: 1 - job info, 2 - address info

# In order to do that we'll also need a 3rd builder, which will serve as a base class.
class PersonBuilder:
    # person param is actually representing the person that is going to build up
    def __init__(self, person=None):
        # avoid the mutation: person = Person()
        if person is None:
            # it allows the subbuilders  to work with an object that is already constructed rather than creating a new person
            self.person = Person()
        else:
            self.person = person

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    # How does the client use the person's job info?
    # so both these properties can be used to jump from one to another.
    @property
    def works(self):
        return PersonJobBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        # making it a fluent interface. so we can add other params
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


if __name__ == '__main__':
    pb = PersonBuilder()
    p = pb \
        .lives \
        .at('123 London Road') \
        .in_city('London') \
        .with_postcode('SW12BC') \
        .works \
        .at('Fabrikam') \
        .as_a('Engineer') \
        .earning(123000) \
        .build()
    print(p)
    person2 = PersonBuilder().build()
    print(person2)
