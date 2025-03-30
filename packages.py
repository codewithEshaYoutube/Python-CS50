"""
Python Packages Overview

A package in Python is a way of organizing related modules together. It is simply a directory containing Python files
and an optional __init__.py file.

Key points:
- A package is a collection of modules.
- A module is a single Python file.
- Packages help organize large projects and promote code reusability.

====================================
Installing Python Packages
====================================
Python packages are usually installed using pip, the package manager for Python. Below are the common commands:

1. Check if pip is installed:
    python -m ensurepip --default-pip

2. Upgrade pip to the latest version:
    python -m pip install --upgrade pip

3. Install a package:
    pip install package_name

4. Install a specific version of a package:
    pip install package_name==1.2.3

5. Install multiple packages from a requirements file:
    pip install -r requirements.txt

6. Uninstall a package:
    pip uninstall package_name

7. List all installed packages:
    pip list

8. Show information about a package:
    pip show package_name

9. Check for outdated packages:
    pip list --outdated

10. Upgrade a specific package:
    pip install --upgrade package_name

====================================
Creating and Using Python Packages
====================================
To create a package:

1. Create a directory (e.g., mypackage/).
2. Add Python modules inside it (e.g., module1.py, module2.py).
3. (Optional) Include an __init__.py file to make it a package.
4. Import and use the package in your scripts:
    from mypackage import module1

Example Directory Structure:
    mypackage/
    ├── __init__.py
    ├── module1.py
    ├── module2.py

Example Content of module1.py:
    def greet(name):
        return f"Hello, {name}!"

Using the package:
    from mypackage.module1 import greet
    print(greet("Alice"))

====================================
Commonly Used Python Packages
====================================
- numpy: Numerical computations
- pandas: Data manipulation and analysis
- matplotlib: Data visualization
- seaborn: Statistical data visualization
- scikit-learn: Machine learning
- tensorflow: Deep learning
- requests: Handling HTTP requests
- flask: Web framework
- django: Full-stack web framework
- sqlalchemy: Database ORM
- scrapy: Web scraping
- beautifulsoup4: HTML parsing
- nltk: Natural Language Processing

====================================
Example of Using a Python Package
====================================
# Example of using the numpy package
import numpy as np

def add_numbers(a, b):
   Adds two numbers using numpy 
    return np.add(a, b)

if __name__ == "__main__":
    result = add_numbers(5, 10)
    print("Sum:", result)

====================================
Additional Resources
====================================
- Official Python Package Index (PyPI): https://pypi.org/
- pip Documentation: https://pip.pypa.io/en/stable/
- Python Packaging Guide: https://packaging.python.org/

"""
