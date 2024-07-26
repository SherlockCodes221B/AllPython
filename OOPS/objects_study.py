class Bike:
    def __init__(self, company_name, price, model):
        self.company_name = company_name
        self.price = price
        self.model = model

bike_obj = Bike("Honda", 3.5, "CBS")
print(bike_obj.price)
bike_obj2 = Bike("RoyalEnfield",4.0,"Himalayan")
print(bike_obj2.model)

''' From Geeks for geeks I got interesting code '''
class Dog:

    # class attribute : Impt
    attr1 = "mammal"

    # Instance attribute: impt
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("My name is {}".format(self.name))

# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class methods
Rodger.speak()
Tommy.speak()


'''
Example for instance variable

'''
'''
class Taxes  
{  
   int count;  
   #...#  
} 
''' 