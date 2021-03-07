from typing import Any, Union


# class Person:
#     indent_size = 2
#
#     def __init__(self, type='', name=''):
#         self.type = type
#         self.name = name
#         self.elements = []  # each html can have any number of children (inner elements in it). so the list to populate them
#
#     def __str(self, indent):
#         lines = []
#         i = ' ' * (indent * self.indent_size)
#         # print(f'class :')
#         # lines.append(f'{CodeBuilder(root_name=Person)}')
#         lines.append(f'{i}self.{self.type} = {self.name}')
#
#         for l in lines:
#             print(f'the lines {l}' )
#
#         for e in self.elements:
#             lines.append(e.__str(indent + 2))
#
#         # lines.append(f'{i}</{self.type}>')
#         return '\n'.join(lines)
#
#     def __str__(self):
#         print(f'class {Person.__name__}:')
#         return self.__str(2)
# (f'{i}def __init__(self, {self.type}, {self.name}):')

class Field:
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def __str__(self):
        return 'self.%s = %s' % (self.name, self.value)

class Person:
    def __init__(self, name):
        self.name = name
        self.elements = []

    def __str__(self):
        lines = ['class %s:' % self.name]
        if not self.elements:
            lines.append('  pass')
        else:
            lines.append('  def __init__(self):')
            for f in self.elements:
                lines.append('    %s' % f)
        return '\n'.join(lines)


class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = Person(root_name)

    def add_field(self, type, name):
        self.__root.elements.append(Field(type, name))
        return self

    def __str__(self):
        return str(self.__root)



cb = CodeBuilder('Person') \
    .add_field('name', '""') \
    .add_field('age', '0')
print(cb)

# class Person:
#     def __init__(self, name, age):
#         self.name = ""
#         self.age = 0