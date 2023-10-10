MyClass = __import__('8-my_class').MyClass
m = MyClass("John")
m.number = 89
print(type(m))
print(m)
print(m.__dict__)