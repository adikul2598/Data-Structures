# Data-Structures

Data Structures are a way of organizing data so that it can be accessed more efficiently depending upon the situation. Data Structures are fundamentals of any programming language around which a program is built.  

## Set

Python Set is an ordered collection of data that is mutable and does not allow any duplicate element. Sets are basically used to include membership testing and   eliminating duplicate entries. The data structure used in this is Hashing, a popular technique to perform insertion, deletion, and traversal in O(1) on average.  

>Set = set([1, 2, 'Gks', 4, 'For', 6, 'eks'])  
>print("\nSet with the use of Mixed Values")  
>print(Set)  

>print("\nElements of set: ")  
>for i in Set:  
>	print(i, end =" ")  
>print()   


>print("Teek" in Set)  

## Frozen Sets

Frozen sets in Python are immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied.  

>normal_set = set(["a", "b","c"])
>print(normal_set)
>frozen_set = frozenset(["e", "f", "g"])
>print("\nFrozen Set")
>print(frozen_set)

## Python Bytearray Operations


>a = bytearray((12, 8, 25, 2))
>print("Creating Bytearray:")
>print(a)
>print("\nAccessing Elements:", a[1])

>a[1] = 3
>print("\nAfter Modifying:")
>print(a)

>a.append(30)
>print("\nAfter Adding Elements:")
>print(a)

## Collection Modules

### Counters

A counter is a sub-class of the dictionary. It is used to keep the count of the elements in an iterable in the form of an unordered dictionary where the key represents   the element in the iterable and value represents the count of that element in the iterable  

>from collections import Counter
	
>print(Counter(['B','B','A','B','C','A','B','B','A','C']))
	
>count = Counter({'A':3, 'B':5, 'C':2})
>print(count)

>count.update(['A', 1])
>print(count)

### OrderedDict

An OrderedDict is also a sub-class of dictionary but unlike a dictionary, it remembers the order in which the keys were inserted.   

>from collections import OrderedDict

>print("Before deleting:\n")
>od = OrderedDict()
>od['a'] = 1
>od['b'] = 2
>od['c'] = 3
>od['d'] = 4

>for key, value in od.items():
>	print(key, value)

>print("\nAfter deleting:\n")
>od.pop('c')
>for key, value in od.items():
>	print(key, value)
  
>print("\nAfter re-inserting:\n")
>od['c'] = 3
>for key, value in od.items():
>	print(key, value)

### DefaultDict

DefaultDict is used to provide some default values for the key that does not exist and never raises a KeyError. Its objects can be initialized using DefaultDict() method by passing the data type as an argument.  

>from collections import defaultdict
>d = defaultdict(int)	
>L = [1, 2, 3, 4, 2, 4, 1, 2]	
>for i in L:	
>	d[i] += 1		
>print(d)

### ChainMap

A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries. When a key is needed to be found then all the dictionaries are searched one by one until the key is found.  

>from collections import ChainMap
>d1 = {'a': 1, 'b': 2}
>d2 = {'c': 3, 'd': 4}
>d3 = {'e': 5, 'f': 6}
>c = ChainMap(d1, d2, d3)
>print(c)
>print(c['a'])
>print(c['g'])

### UserDict

UserDict is a dictionary-like container that acts as a wrapper around the dictionary objects.  

>from collections import UserDict

>class MyDict(UserDict):
	
	>def __del__(self):
	>	raise RuntimeError("Deletion not allowed")
	>def pop(self, s = None):
	>	raise RuntimeError("Deletion not allowed")
		>def popitem(self, s = None):
	>	raise RuntimeError("Deletion not allowed")
	>d = MyDict({'a':1,
>	'b': 2,
>	'c': 3})
>print("Original Dictionary")
>print(d)
>d.pop(1)

## Linked List

A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.  
A linked list is represented by a pointer to the first node of the linked list. The first node is called the head.  

>class Node:  
>
>	
>	def __init__(self, data):  
>		self.data = data   
>		self.next = None
>						  
>
>
>class LinkedList:  
>	
>	def __init__(self):  
>		self.head = None  
