'''
Counter class is a special type of object data-set provided with the collections module in Python3. 
Collections module provides the user with specialized container datatypes, thus, providing an alternative to Python’s general-purpose built-ins like dictionaries, lists, and tuples. 
'''
'''
To count several different objects at once, you can use a Python dictionary. The dictionary keys will store the objects you want to count. 
The dictionary values will hold the number of repetitions of a given object, or the object’s count.
'''
word = "mississippi"
counter = {}

for letter in word:
    if letter not in counter:
        counter[letter] = 0
    counter[letter] += 1


counter

'''
Another way to count objects with a dictionary is to use dict.get() with 0 as a default value

'''
word = "mississippi"
counter = {}

for letter in word:
    counter[letter] = counter.get(letter, 0) + 1


counter


'''
You can also use defaultdict from collections to count objects within a loop

'''

from collections import defaultdict

word = "mississippi"
counter = defaultdict(int)

for letter in word:
    counter[letter] += 1


counter


''' Using Counter '''

from collections import Counter

# Use a string as an argument
Counter("mississippi")


# Use a list as an argument
Counter(list("mississippi"))
