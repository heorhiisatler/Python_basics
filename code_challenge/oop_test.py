class MyClass:
    """A simple example class"""
    i = 12345
    name = ""
    
    def f(self):
        return 'hello world'

    
    def __init__(self, name):
        self.name = name
        


a = MyClass("Test")
b= MyClass("Test")
a.counter = 1
print(a.counter)
# print(b.counter) -> Exeption
# del x.counter
print(a.i, a.name)
