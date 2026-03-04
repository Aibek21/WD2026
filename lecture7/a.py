print('hello world')

# this is comments


a = True
b = False
c = None

print(type(a))

a = 'Hello world'

print(type(a))

a_str = 'Hello "asd" world'
b_str = "Hello \"asd\" world"
c_str = """Hello 
world"""
print(a_str)
print(b_str)
print(c_str)

a_str = "Hello world"
print(a_str[1:5:2])
print(a_str[-1])

print("{0}: {1}".format('hello', 'world'))
print("{a}: {b}".format(a='hello', b='world'))

arr = [1, True]  # list is mutable
arr2 = (1, True)  # tuple is immutable

arr.append('hello')
print(arr)

# arr2[1] = False
# print(arr2.append('world'))

arr3 = set([1, 2, 1])
print(arr3)

a_dict = {'username': 'admin', 'position': 'CEO'}
print(a_dict['username'])
print(a_dict.get('username'))

print(a_dict.keys())
print(a_dict.values())

print(a_dict.items())

for key, value in a_dict.items():
    print(key, value)

if 'name' in a_dict:
    print(a_dict['name'])
elif 'username' in a_dict:
    print(a_dict['username'])
else:
    print('no name')


def add(a=1, b=2, *args, **kwargs):
    print(args)
    print(kwargs)
    return a + b


print(add(5, 6, 1, 2, 3, 4, 5, name='some name'))


class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_of_shape(self):
        return self.width * self.height


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)


rectangle = Rectangle(100, 200)
print(rectangle.area())
