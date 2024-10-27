
def deco1(input):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('naveen1')
            return func(*args, **kwargs)
        return wrapper
    print(input)
    return decorator

def deco2(input):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('naveen1')
            return func(*args, **kwargs)
        return wrapper
    print(input, 'klasojaj')
    return decorator

@deco2('input2')
@deco1('input1')
def practice():
    print('naveen2')

practice()
def greet(name: int, age: int) -> int:
    return name/age

# Calling the function
greet(70, 30)

from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering")
    yield
    print("Exiting")

with my_context():
    print("Inside")

class A():
    def __init__(self, val):
        self.value=val
    def __str__(self):
        return f'Value: {self.value}'


obj = A(10)
print(obj)

obj = [
    {'name': 'naveen', 'age': 20},
    {'name': 'naveen0', 'age': 19},
    {'name': 'naveen1', 'age': 42},
]
def even_age_generator(students):
    for student in students:
        if student['age'] % 2 == 0:
            yield student
print(sorted(obj, key=lambda item: item['age']))
print(filter(lambda x: x['age']%2==0, obj))
hey = even_age_generator(obj)
# for x in even_age_generator(obj):
#     print(x)
print(next(hey))
print(next(hey))
# print(next(hey))

def second_element(item):
    return item[1]

pairs = [(1, 2), (3, 1), (5, 0), (7, 9)]
sorted_pairs_desc = sorted(pairs, key=second_element, reverse=True)
print(sorted_pairs_desc)  # Output: [(7, 9), (1, 2), (3, 1), (5, 0)]

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(my_list[::-2])

# Iterator Example
class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            result = self.count
            self.count += 1
            return result
        else:
            self.count = 0
            raise StopIteration

it = MyIterator(5)

# Generator Example
def my_generator(limit):
    count = 0
    while count < limit:
        yield count
        count += 1

gen = my_generator(5)
print(type(gen))

for x in gen:
    print(x)
print('**'*6)
for x in gen:
    print(x)

# for x in it:
#     print(x)
# print('**'*6)
# for x in it:
#     print(x)

def h(name: str = 'naveen') -> None:
    """Prints the provided name, defaulting to 'naveen' if none is given."""
    print(name)
def h1(name):
    print(name)

h(9)
h1('alhiho')