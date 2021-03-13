# If you want to build a simple html paragraph using a list
text = 'hello'
parts = ['<p>', text, '</p>']
# print(''.join(parts))

# you're given a bunch of words and you want to make a html list out of these words.
# designing a html page with html tags
words = ['hello', 'world']
parts = ['<ul>']
for w in words:
    parts.append(f' <li>{w}</li>')
# if someone forgets this part or the previous, it will be an error.
parts.append('</ul>')
# print('\n'.join(parts))


# to avoid the errors we need to outsource the process of constructing different parts of html (lists, paragraphs anything) to a builder.
# it's better to work with OOP structures

class HtmlElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        self.name = name
        self.text = text
        self.elements = []  # each html can have any number of children (inner elements in it). so the list to populate them

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

        # defining an str method by calling an internal method __str with the indent = 0
        # we get the indentation regardless how many nesting layers we have in our html
        # It's just a helper which helps us build the html.
    def __str__(self):
        return self.__str(0)

    # that's how you can get started. Line 92 instead of 91
    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    # it takes the htmlelement and it going to construct it and build it from scratch
    # __root = HtmlElement()

    def __init__(self, root_name):
        self.root_name = root_name
        # specific instance of the element we're building
        self.__root = HtmlElement(name=root_name)

    # not fluent
    # this method helps to add a child to current root
    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    # fluent
    # it's similar to an ordinary interface except you can chain it
    # you can have 2 add_child() calls one after another
    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        # that's how you can chain invocations one after another
        return self

    def clear(self):
        self.__root = HtmlElement(name=self.root_name)

    # expose the object you're building up with dunder.
    def __str__(self):
        return str(self.__root)



# ordinary non-fluent builder
builder = HtmlBuilder('ul')
# builder = HtmlElement.create('ul')
builder.add_child('li', 'hello')
builder.add_child('li', 'world')
print('Ordinary builder:')
# print(builder)

# fluent builder
builder.clear()
builder.add_child_fluent('li', 'hello') \
    .add_child_fluent('li', 'world')
print('Fluent builder:')
print(builder)
