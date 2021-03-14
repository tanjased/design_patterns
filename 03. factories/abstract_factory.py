# ABSTRACT FACTORY
# If you have a hierarchy of types, then you have a corresponding hierarchy of factories.
# So at some point you'll have an abstract factory as a base class of another factory.
from abc import ABC
from enum import Enum, auto


# abstract base class
class HotDrink(ABC):
    def consume(self):
        pass


# we make here concrete implementation of the HotDrink class
class Tea(HotDrink):
    def consume(self):
        print('This tea is delicious.')


class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious.')


# Child class operations are so sophisticated, that you need a factory to run them. ?
# in addition to hierarchy of classes, we'll hierarchy of factories
class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water,'
              f'pour {amount}ml, enjoy!')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind beans, boil water,'
              f'pour {amount}ml, enjoy!')
        return Coffee()


# How do we actually make a drink?
# A scenario

### This part is modified. New approach
# This approach breaks the OCP, because when you make a new drink, you have to go this class and modify it
class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()  # auto-numbering
        TEA = auto()

    # initialize HotDrinkMachine. A factory for every available drink type
    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                # get the name of the drink
                name = d.name[0] + d.name[:1].lower()
                # make a factory name out of it
                factory_name = name + 'Factory'
                # create an factory instance
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))


    # interactive display
    def make_drink(self):
        print('Available drinks:')
        for f in self.factories:
            print(f[0])  # here we print 'name' in the tuple

        s = input(
            f'Pick drink (0-{len(self.factories) - 1}): ')  # the range of drinks (names) goes from 0 to number of factories - 1
        idx = int(s)  # turn it into index
        s = input(f'Specify amount: ')
        amount = int(s)
        return self.factories[idx][1].prepare(amount)  # it's clear


# but we need to make a drink out of our input, make_drink()
def make_drink(type):
    if type == 'tea':
        return TeaFactory().prepare(200)  # why do we type TeaFactory() instead of TeaFactory ?
    elif type == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None


if __name__ == '__main__':
    # entry = input('What kind of drink would you like? ')
    # drink = make_drink(entry)
    # drink.consume()
    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()

# but we didn't really use the abstract class. In this case the only reason why we used it is
# that we mandate a method which is inherited and developed in child classes.
