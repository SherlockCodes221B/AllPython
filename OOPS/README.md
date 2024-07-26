# OOP in Python

## what is oop?

Object-oriented programming (OOP) is a method of structuring a program by bundling related properties and behaviors into individual objects.<br>
<b>Object-oriented programming</b> is a programming paradigm that provides a means of structuring programs so that properties and behaviors are bundled into individual objects.

## Concepts

### Class and Objects

<b>Classes</b><br>
Collection of objects. It is the blueprint or prototype from which objects are created<br>
Keyword : <b> class </b><br/>
Attributes : Variables belong to the class and they are always public
```
class ClassName:
    # Statement1
    # Statement2
    .
    .
    # Statementn
```


<b>objects</b><br>
Entity having state and behaviour associated with it. object can hold other objects.It consists of :-
<ul>
<li> State ----> Reflects properties of the objects. Represents attributes of an objects</li>
<li> Behaviour -----> Reflects the reponse of one object to other objects</li>
<li> Identity ------> Gives unique name to an object and enables one object to interact with other objects</li>
</ul>

```
object = classname(parameters)
```

#### Combining class and objects:<br>
Creating class and object with class and instance attributes

```
class Bike:
    def __init__(self, company_name, price, model):
        self.company_name = company_name
        self.price = price
        self.model = model

bike_obj = Bike("Honda", 3.5, "CBS")
print(bike_obj.price)
bike_obj2 = Bike("RoyalEnfield",4.0,"Himalayan")
print(bike_obj2.model)
```

**_NOTE:_** 
```
def __init__(self):
    pass
```
<b>__init\__(self)</b> :  is the constructor for a class. This method gets called after memory for the object is allocated
<b>self</b>: The self variable refers to the object itself.
Let's say you have a class ClassA which contains a method methodA defined as:
```
class ClassA:
    def methodA(self, arg1, arg2):
        ... # do something
````
and objectA is an instance of this class.

Now when objectA.methodA(arg1, arg2) is called, python internally converts it for you as:
```
ClassA.methodA(objectA, arg1, arg2)
```

## Inheritence

Inheritance is the capability of one class to derive or inherit the properties from another class.The class that derives properties is called the derived class or child class and the class from which the properties are being derived is called the base class or parent class.It has 3 types :-
<ol>
<li>Single Inheritence :  One parent to one child , the properties are shared</li>
<li>Multilevel Inheritence :  One immediate parent one child , the properties are shared</li>
<li> Hierarchical Inheritence : more than one derived class to inherit properties from a parent class.</li>
<li> Multiple Inheritence :  One child multiple parent classes.
</ol>

```
class Animal:
    # attribute and method of the parent class
    name = ""
    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):
    # New method in subclass
    def display(self):
        # access name attribute of superclass using self
        print("My name is ", self.name)
# create an object of the subclass
labrador = Dog()
# access superclass attribute and method 
labrador.name = "Rohu"
labrador.eat()
# call subclass method 
labrador.display()
```

## Polymorphism

Polymorphism simply means having many forms. it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
<ul><li>Function Polymorphism : --> For strings len() returns the number of characters<br> &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; --> For Tuples len() returns number of items</li>
<li>Class Polymorphism : multiple classes with the same method name.Given in example script</li>
</ul>

## Encapsulation

wrapping data and the methods that work on data within one unit.Here we have access modifiers
<ul>
<li> Public access modifier : The members of a class that are declared public are easily accessible from any part of the program. All data members and member functions of a class are public by default. 
Example code :<br>

```
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
s = Student("John",20)
s.display() 
```
</li>
<li>
Private access modifier( double underscore __ ) : Class properties and methods with private access modifier can only be accessed within the class where they are defined and cannot be accessed outside the class. Example Code:

```
class BankAccount:
   def __init__(self, account_number, balance):
      self.__account_number = account_number
      self.__balance = balance
    
   def __display_balance(self):
      print("Balance:", self.__balance)

b = BankAccount(1234567890, 5000)
b.__display_balance() 
```
</li>
<li>
Protected access modifier ( single underscore _) : Class properties and methods with protected access modifier can be accessed within the class and from the class that inherits the protected class. Code example

```
class Person:
   def __init__(self, name, age):
      self._name = name
      self._age = age
    
   def _display(self):
      print("Name:", self._name)
      print("Age:", self._age)

class Student(Person):
   def __init__(self, name, age, roll_number):
      super().__init__(name, age)
      self._roll_number = roll_number
    
   def display(self):
      self._display()
      print("Roll Number:", self._roll_number)

s = Student("John", 20, 123)
s.display()
``` 
</li>
</ul>

## Data Abstraction

Familiar with that "what function does" but they don't know "how it does.".Hide the internal functionality of the function from the users.

```
from abc import ABC  
class ClassName(ABC):
    #---
```
Abstarct class : Unlike the other high-level language, Python doesn't provide the abstract class itself. We need to import the abc module, which provides the base for defining Abstract Base classes (ABC).We use the @abstractmethod decorator to define an abstract