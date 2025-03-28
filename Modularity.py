"""
modularity.py - A complete Python module demonstrating modularity.
This module includes:
✔️ Arithmetic Functions
✔️ String Manipulation
✔️ File Handling
✔️ System Utilities
✔️ Demonstration of Different Import Methods
"""

import os
import sys
import random

# -----------------------------
# 🔢 1️⃣ Arithmetic Operations
# -----------------------------
def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Returns the difference of two numbers."""
    return a - b

# -----------------------------
# 🔤 2️⃣ String Utilities
# -----------------------------
def reverse_string(s: str) -> str:
    """Returns the reversed version of a given string."""
    return s[::-1]

def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome."""
    return s == s[::-1]

# -----------------------------
# 📂 3️⃣ File Handling
# -----------------------------
def write_to_file(filename: str, content: str):
    """Writes content to a file."""
    with open(filename, "w") as file:
        file.write(content)

def read_from_file(filename: str) -> str:
    """Reads content from a file."""
    if not os.path.exists(filename):
        return "Error: File not found!"
    with open(filename, "r") as file:
        return file.read()

# -----------------------------
# ⚙️ 4️⃣ System Utilities
# -----------------------------
def get_system_info():
    """Returns the system platform and version."""
    return {
        "Platform": sys.platform,
        "Python Version": sys.version
    }

def generate_random_number(start: int, end: int) -> int:
    """Returns a random number within the given range."""
    return random.randint(start, end)

# -----------------------------
# 🏁 5️⃣ Execution Control (Direct Execution)
# -----------------------------
if __name__ == "__main__":
    print("📌 Running modularity.py as a standalone script!")
    print(f"🔢 Addition: 5 + 3 = {add(5, 3)}")
    print(f"🔤 Reverse String: 'hello' → {reverse_string('hello')}")
    write_to_file("test.txt", "Hello, Modular World!")
    print(f"📂 Read File: {read_from_file('test.txt')}")
    print(f"⚙️ System Info: {get_system_info()}")
    print(f"🎲 Random Number (1-10): {generate_random_number(1, 10)}")

# 🏁 5️⃣ Demonstrating Different Import Methods
# -----------------------------

# ✅ 1. Importing the entire module
print("\n✅ 1. Importing the entire module")
import modularity  # Import itself (for demonstration)
print(f"🔢 Addition (10+5): {modularity.add(10, 5)}")
print(f"🔤 Reverse String ('Python'): {modularity.reverse_string('Python')}")

# ✅ 2. Importing specific functions
print("\n✅ 2. Importing specific functions")
from modularity import add, reverse_string
print(f"🔢 Addition (4+6): {add(4, 6)}")
print(f"🔤 Reverse String ('world'): {reverse_string('world')}")

# ✅ 3. Importing with an alias
print("\n✅ 3. Importing with an alias")
import modularity as mod
print(f"🔢 Subtraction (10-4): {mod.subtract(10, 4)}")

# ✅ 4. Running the module directly
if __name__ == "__main__":
    print("\n📌 Running modularity.py as a standalone script!")
    print(f"📂 File Writing Example: Saving 'Hello Modular World!' to test.txt")
    write_to_file("test.txt", "Hello Modular World!")
    print(f"📂 File Reading Example: {read_from_file('test.txt')}")
    print(f"⚙️ System Info: {get_system_info()}")
    print(f"🎲 Random Number (1-10): {generate_random_number(1, 10)}")
