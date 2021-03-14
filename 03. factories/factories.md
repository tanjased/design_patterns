**Factory method** is a static method which creates objects

Why do we need **factories**?
- object creation logic becomes too convoluted
- initializer is not descriptive
    - name is always __init__
    - cannot overload with same sets of arguments with different names
    - can turn into 'optional parameter hell' (when you add more and more arguments - some are optional, some have default values)
- Wholesale object creation (non-piecewise, unlike Builder) can be outsourced to 
    - A separate method (Factory method), typically static methods
    - That may exist in a separate class (Factory)
    - Can create a hierarchy of factories with Abstract Factory
    

_**FACTORY**_ is a component responsible for wholesale (not piecewise) creation of objects


It's typically any method which creates an object.


**ABSTRACT FACTORY notes are in abstract_factory.py


