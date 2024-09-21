class animal:
    # __slots__ = ['__name', 'value', '_val'] # restict he variables to create the class
    def __init__(self, name):
        self.__name=name # private
        self.value = name # public
        self._val = name #protected

    # without property setter or any other methods will not work 
    @property
    def name1(self):
        return self.__name
    
    @name1.setter
    def name(self, name):
        self.__name = name
    
    @name1.setter
    # it may not be variable name, this will also work
    def change(self, name):
        self.__name = name
    
    def speak(self):
        print('bow bow')


dog = animal('dog')

# print(dog._val, 'protected variable')
# print(dog._animal__name, 'way to access private variable')

# print(dog.name)
# dog.name1='cat'
# print(dog.name)

# print(getattr(dog, 'name'))
# print(getattr(dog, 'value', 'naveen'))
# print(getattr(dog, 'speak'))

class Car:
    wheels = 4  # Class attribute shared by all instances

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # these are only have class level access not an isntance
    @classmethod
    def car_wheels(cls):
        return f"All cars have {cls.wheels} wheels by default"
    
    # these are like an normal functions which does not have access to class or instances 
    @staticmethod
    def change():
        return 'changed'

# Called on the class itself, not an instance
# print(Car.car_wheels())  # Output: All cars have 4 wheels by default

# print(dir(Car))
# print(Car.__class__)

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        return f"Vehicle brand: {self.brand}"
    
    def show_details(self):
        return f"Car model: parent"


class Car(Vehicle):  # Inheriting Vehicle class
    def __init__(self, brand, model):
        super().__init__(brand)  # Calling parent class constructor
        self.model = model

    def show_details(self):
        return f"Car model: {self.model}, {self.show_brand()}"


car = Car("Toyota", "Camry")
print(car.show_details())  # Car model: Camry, Vehicle brand: Toyota

#decorators 
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('start')
        print(func.__name__)
        func(*args, **kwargs)
        print('end')
    return wrapper

def my_decorator1(name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('start')
            print(name)
            func(*args, **kwargs)
            print('end')
        return wrapper
    return decorator

@my_decorator
def callfunc():
    print('called')

@my_decorator1('jjjj')
def callfunc1():
    print('called')

callfunc()
# callfunc1()

class A:
    def process(self):
        print("Processing in A")

class B(A):
    def process(self):
        print("Processing in B")

class C(A):
    def process(self):
        print("Processing in C")

class D(B, C):
    pass

# Usage
d = D()
d.process()  # Output: Processing in B

# Checking MRO
print(D.__mro__)  # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Robot:
    def speak(self):
        return "Beep Boop"

# A function that relies on duck typing
def make_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
robot = Robot()

# method overloading 
make_speak(dog)   # Output: Woof!
make_speak(cat)   # Output: Meow!
make_speak(robot) # Output: Beep Boop

