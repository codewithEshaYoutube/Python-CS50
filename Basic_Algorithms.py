 '''
binary search
'''
from operator import itemgetter


def binary_search(list,item):
    low = 0
    high = len (list) - 1
    while low<= high:
        mid=(low+high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
            return None
my_list=[1,2,3,4,5,6,7,8,9,10]
print (f"The index is",(binary_search(my_list,3)))
print (f"The index is",(binary_search(my_list,8)))
print (f"The index is",(binary_search(my_list,17)))

# Scenario 1.4: You have a name, and you want to find the person’s phone number in the phone book.

# Unsorted phone book (as an example)
phone_book_unsorted = [
    ("John", "123-456-7890"),
    ("Alice", "987-654-3210"),
    ("Bob", "555-123-4567")
]

# Linear search to find the phone number for a given name
def linear_search_name_to_number(name, phone_book):
    for entry in phone_book:
        if entry[0] == name:
            return entry[1]  # Return phone number
    return None  # Return None if name not found

# Example usage
name_to_find = "Alice"
print(f"Phone number of {name_to_find}: {linear_search_name_to_number(name_to_find, phone_book_unsorted)}")

# Scenario 1.5: You have a phone number, and you want to find the person’s name in the phone book.

# Linear search to find the name for a given phone number
def linear_search_number_to_name(phone_number, phone_book):
    for entry in phone_book:
        if entry[1] == phone_number:
            return entry[0]  # Return name
    return None  # Return None if phone number not found

# Example usage
phone_number_to_find = "555-123-4567"
print(f"Name for phone number {phone_number_to_find}: {linear_search_number_to_name(phone_number_to_find, phone_book_unsorted)}")

# Scenario 1.6: You want to read the numbers of every person in the phone book.

# Reading all phone numbers (simply iterating over all entries)
def read_all_numbers(phone_book):
    numbers = [entry[1] for entry in phone_book]
    return numbers

# Example usage
print("All phone numbers:", read_all_numbers(phone_book_unsorted))

# Scenario 1.7: You want to read the numbers of just the 'A's.

# Linear search to find phone numbers starting with 'A'
def read_numbers_starting_with_a(phone_book):
    numbers = [entry[1] for entry in phone_book if entry[0].startswith('A')]
    return numbers

# Example usage
print("Phone numbers of people starting with 'A':", read_numbers_starting_with_a(phone_book_unsorted))
