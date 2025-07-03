# list:- List is a collection which is ordered and changeable. Allows duplicate members.
# tuple:- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# set:- Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
# dict:- Dictionary is a collection which is unordered, changeable, and indexed. No duplicate members.  
# str:- String is a collection which is ordered and unchangeable. Allows duplicate members.
# bool:- Boolean is a data type that can only have two values: True or False.
# int:- Integer is a data type that represents whole numbers, both positive and negative, without any decimal points.
# float:- Float is a data type that represents real numbers, allowing for decimal points.
# complex:- Complex is a data type that represents complex numbers, which have a real and an imaginary part.
# None:- None is a special constant in Python that represents the absence of a value or a null value.
# bytes:- Bytes is a data type that represents immutable sequences of bytes, often used for binary data.
# bytearray:- Bytearray is a mutable sequence of bytes, allowing for modification of the byte data.
# frozenset:- Frozenset is an immutable version of a set, meaning it cannot be changed after creation.
# range:- Range is a built-in function that generates a sequence of numbers, commonly used in loops.
# memoryview:- Memoryview is a built-in function that allows direct access to the memory of an object without copying it.
# Example of each data type in Python:-

# list = list in python will always be defined by []. JavaScript's array is equivalent to python's list
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]
len(my_list)  # Output: 5   

# tuple = tuple in python will always be defined by (). JavaScript's array is equivalent to python's tuple
my_tuple = (1, 2, 3, 4, 5)  
print(my_tuple)  # Output: (1, 2, 3, 4, 5)
len(my_tuple)  # Output: 5  


# set = set in python will always be defined by {}. JavaScript's Set is equivalent to python's set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
len(my_set)  # Output: 5

# dict = dict in python will always be defined by {}. JavaScript's Object is equivalent to python's dict
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
len(my_dict)  # Output: 3


# str = str in python will always be defined by "". JavaScript's String is equivalent to python's str
my_str = "Hello, Harsh!"
print(my_str)  # Output: Hello, World!
len(my_str)  # Output: 13   


# bool = bool in python will always be defined by True or False. JavaScript's Boolean is equivalent to python's bool
my_bool = True  
print(my_bool)  # Output: True
len(my_bool)  # Output: 4 (length of the string representation of True) 


# int = int in python will always be defined by 1, 2, 3, etc. JavaScript's Number is equivalent to python's int
my_int = 42
print(my_int)  # Output: 42
len(str(my_int))  # Output: 2 (length of the string representation of 42)   


# float = float in python will always be defined by 1.0, 2.5, 3.14, etc. JavaScript's Number is equivalent to python's float
my_float = 3.14
print(my_float)  # Output: 3.14
len(str(my_float))  # Output: 4 (length of the string representation of 3.14)

# complex = complex in python will always be defined by 1+2j, 3-4j, etc. JavaScript does not have a direct equivalent
my_complex = 1 + 2j
print(my_complex)  # Output: (1+2j)
len(str(my_complex))  # Output: 7 (length of the string representation of (1+2j))


# bytes = bytes in python will always be defined by b'bytes'. JavaScript does not have a direct equivalent
my_bytes = b'bytes' 
print(my_bytes)  # Output: b'bytes'
len(my_bytes)  # Output: 5 (length of the byte string 'bytes')  


# bytearray = bytearray in python will always be defined by bytearray(b'bytes'). JavaScript does not have a direct equivalent
my_bytearray = bytearray(b'bytes')  
print(my_bytearray)  # Output: bytearray(b'bytes')
len(my_bytearray)  # Output: 5 (length of the byte array 'bytess')


# None = None in python will always be defined by None. JavaScript's null is equivalent to python's None
my_none = None  
print(my_none)  # Output: None
len(str(my_none))  # Output: 4 (length of the string representation of None)
# range = range in python will always be defined by range(1, 10). JavaScript does not have a direct equivalent
my_range = range(1, 10) 
print(list(my_range))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
len(my_range)  # Output: 9 (length of the range from 1 to 10, excluding 10)


# frozenset = frozenset in python will always be defined by frozenset({1, 2, 3}). JavaScript does not have a direct equivalent
my_frozenset = frozenset({1, 2, 3})




