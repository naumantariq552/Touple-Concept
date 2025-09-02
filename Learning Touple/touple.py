# 🚀 Python Tuple Basics — Easy Guide

# Normal Tuple
my_tuple = (10, 20, 30, 40, 50)
print("Normal Tuple:", my_tuple)

# Single Tuple (must use a comma!)
single_tuple = (5,)
print("Single Tuple:", single_tuple, "Type:", type(single_tuple))

# Indexing
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing
print("Slicing [1:4]:", my_tuple[1:4])

# Count & Index Methods
numbers = (1, 2, 2, 3, 2, 4)
print("Tuple:", numbers)
print("Count of 2:", numbers.count(2))
print("Index of 3:", numbers.index(3))
