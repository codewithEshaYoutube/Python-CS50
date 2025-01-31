   # Introduction to Data Types in Python

# 1. **Numeric Types**:
# - **int**: Integer values, represents whole numbers.
# - **float**: Floating-point numbers, represents decimal values.
# - **complex**: Complex numbers, consists of real and imaginary parts.

# Example of Numeric Types:
x = 10           # int - Represents a whole number
y = 3.14         # float - Represents a decimal number
z = 2 + 3j       # complex - Represents a complex number (real + imaginary)

# 2. **Sequence Types**:
# - **list**: An ordered collection of items that can be of different data types. Mutable (can be changed).
# - **tuple**: An ordered collection of items, immutable (cannot be changed after creation).
# - **range**: Represents an immutable sequence of numbers, typically used in loops.

# Example of Sequence Types:
my_list = [1, 2, 3, 'Python']  # list - Can store items of different data types
my_tuple = (4, 5, 6)            # tuple - Ordered and immutable collection
my_range = range(5)             # range - Generates a sequence of numbers from 0 to 4

# 3. **Text Type**:
# - **str**: A string is a sequence of characters enclosed in single, double, or triple quotes.

# Example of Text Type:
my_string = "Hello, World!"     # str - A sequence of characters

# 4. **Mapping Type**:
# - **dict**: A dictionary is a collection of key-value pairs. Keys must be unique and immutable.

# Example of Mapping Type:
my_dict = {'name': 'Alice', 'age': 25}  # dict - A collection of key-value pairs

# 5. **Set Types**:
# - **set**: An unordered collection of unique items. Mutable (can be changed).
# - **frozenset**: Similar to a set but immutable.

# Example of Set Types:
my_set = {1, 2, 3}       # set - Unordered collection of unique items
my_frozenset = frozenset([4, 5, 6])  # frozenset - Immutable set

# 6. **Boolean Type**:
# - **bool**: Represents either True or False.

# Example of Boolean Type:
is_active = True        # bool - Represents a True value
is_completed = False    # bool - Represents a False value

# 7. **Binary Types**:
# - **bytes**: Immutable sequence of bytes.
# - **bytearray**: Mutable sequence of bytes.
# - **memoryview**: A view object that exposes an array’s buffer interface.

# Example of Binary Types:
my_bytes = b'Hello'       # bytes - Immutable sequence of bytes
my_bytearray = bytearray([65, 66, 67])  # bytearray - Mutable sequence of bytes
my_memoryview = memoryview(my_bytes)  # memoryview - View into the byte data

# Example combining different data types:
# Let's print out various data types to show how they work together:

print(f"Integer: {x}, Float: {y}, Complex: {z}")
print(f"List: {my_list}, Tuple: {my_tuple}, Range: {list(my_range)}")
print(f"Dictionary: {my_dict}")
print(f"Set: {my_set}, Frozenset: {my_frozenset}")
print(f"Boolean: {is_active}")
print(f"Bytes: {my_bytes}")
print(f"Bytearray: {my_bytearray}")
print(f"Memoryview: {my_memoryview}")

# Data Type Summary:
# - **int**: Integer numbers, example: x = 5
# - **float**: Decimal numbers, example: y = 3.14
# - **complex**: Complex numbers, example: z = 2 + 3j
# - **str**: Text (string), example: name = "John"
# - **list**: Ordered and mutable collection, example: my_list = [1, 2, 3]
# - **tuple**: Ordered and immutable collection, example: my_tuple = (1, 2, 3)
# - **dict**: Key-value pairs, example: my_dict = {'key': 'value'}
# - **set**: Unordered collection of unique items, example: my_set = {1, 2, 3}
# - **frozenset**: Immutable set, example: my_frozenset = frozenset([1, 2, 3])
# - **bool**: True or False values, example: is_active = True
# - **bytes**: Immutable sequence of bytes, example: my_bytes = b'Hello'
# - **bytearray**: Mutable sequence of bytes, example: my_bytearray = bytearray([65, 66])
# - **memoryview**: View object for binary data, example: my_memoryview = memoryview(my_bytes)

# Key Points:
# - Python supports dynamic typing, meaning variables don’t need a predefined type.
# - Python automatically determines the type based on the assigned value.
# - Each data type serves a different purpose, from numeric calculations to managing collections of data.

# Conclusion:
# Python has a wide variety of data types, each serving different use cases.
# Understanding these data types will help you write more efficient and readable code in both general software development and data science.

