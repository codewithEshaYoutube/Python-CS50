# Loops in Python: A guide for beginners

# 1. **For Loop** - Used to iterate over a sequence (e.g., list, tuple, string, or range)

# Example 1: Iterating over a list of fruits
fruits = ["Apple", "Banana", "Orange", "Mango"]
# A for loop that prints each fruit in the list
for fruit in fruits:
    print(fruit)

# Example 2: Using a for loop with range() to print numbers from 0 to 4
for i in range(5):
    print(i)

# 2. **While Loop** - Runs as long as the condition is true

# Example 1: Using a while loop to count numbers from 0 to 4
count = 0
while count < 5:
    print(count)
    count += 1  # Increment the count by 1

# 3. **Breaking and Continuing Loops** - You can stop a loop or skip certain iterations

# Example 1: Using break to stop the loop when the value reaches 5
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)

# Example 2: Using continue to skip printing the number 5
for i in range(10):
    if i == 5:
        continue  # Skip when i is 5
    print(i)

# 4. **Nested Loops** - A loop inside another loop

# Example: Nested for loop to iterate over rows and columns
for i in range(3):  # Outer loop (rows)
    for j in range(2):  # Inner loop (columns)
        print(f"Row {i}, Column {j}")

# 5. **Explanation of each loop**:
# - **For loop**: Executes a block of code for each item in a sequence (e.g., a list or a range).
# - **While loop**: Executes a block of code as long as the specified condition is true.
# - **Break**: Terminates the loop when a condition is met.
# - **Continue**: Skips the current iteration of the loop when a condition is met.
# - **Nested loop**: A loop inside another loop that allows iteration over multi-dimensional data (like 2D grids).


