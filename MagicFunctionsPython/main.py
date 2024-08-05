'''
All the available magic methods support built-in features and play specific roles in the language. 
For example, built-in types such as lists, strings, and dictionaries implement most of their core functionality using magic methods. 
In your custom classes, you can use magic methods to make callable objects, define how objects are compared, 
tweak how you create objects, and more.
'''

# Basic adding using objects
print((5).__add__(2))

# Initaliser just like a constructor in other languages
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# When you call a class constructor to create a new instance of a class, 
# Python implicitly calls the .__new__() method as the first step in the instantiation process.
#This method is responsible for creating and returning a new empty object of the underlying class. 
# Python then passes the just-created object to .__init__() for initialization.

class Storage(float):
    def __new__(cls, value, unit):
        instance = super().__new__(cls, value)
        instance.unit = unit
        return instance
    
# The .__str__() special method returns a human-readable string representation of the object at hand. 
# Python calls this method when you call the built-in str() function, passing an instance of the class as an argument.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"I'm {self.name}, and I'm {self.age} years old."
    
# The .__repr__() method returns a string representation of an object that’s targeted at the developer.
class Person:
    # ...
    def __repr__(self):
        return f"{type(self).__name__}(name='{self.name}', age={self.age})"

# Operator overloading
'''
    Operator	    Supporting Method
        +	      .__add__(self, other)
        -	      .__sub__(self, other)
        *	      .__mul__(self, other)
        /	      .__truediv__(self, other)
        //	      .__floordiv__(self, other)
        %	      .__mod__(self, other)
        **  	  .__pow__(self, other[, modulo])
        <	      .__lt__(self, other)
        <=	      .__le__(self, other)
        ==	      .__eq__(self, other)
        !=	      .__ne__(self, other)
        >=	      .__ge__(self, other)
        >	      .__gt__(self, other)
'''
class Distance:
    _multiples = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1_000,
    }

    def __init__(self, value, unit="m"):
        self.value = value
        self.unit = unit.lower()

    def to_meter(self):
        return self.value * type(self)._multiples[self.unit]

    def __add__(self, other):
        return self._compute(other, "+")

    def __sub__(self, other):
        return self._compute(other, "-")

    def _compute(self, other, operator):
        operation = eval(f"{self.to_meter()} {operator} {other.to_meter()}")
        cls = type(self)
        return cls(operation / cls._multiples[self.unit], self.unit)

disk_1 = Storage(500, "GB")
disk_2 = Storage(1000, "GB")
disk_3 = Storage(1, "TB")
disk_1 + disk_2
disk_2 + disk_3
'''
disk_1 + disk_2
1500.0

>>> disk_2 + disk_3
Traceback (most recent call last):
    ...
TypeError: incompatible units: 'GB' and 'TB'

>>> disk_1 + 100
Traceback (most recent call last):
    ...
TypeError: unsupported operand for +: 'Storage' and 'int'


'''