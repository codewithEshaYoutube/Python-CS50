# Step 1: Import necessary libraries
# We will need these libraries to perform operations on data, visualizations, and machine learning.

import pandas as pd  # Pandas is a powerful library for data manipulation and analysis.
import numpy as np  # NumPy is used for numerical operations on arrays and matrices.
import matplotlib.pyplot as plt  # Matplotlib is used for creating static, animated, and interactive visualizations.
import seaborn as sns  # Seaborn is built on top of Matplotlib and provides a high-level interface for statistical graphics.

# Step 2: Creating basic variables in Python
# We begin by understanding simple data types and variables in Python.

x = 10  # Integer data type: Represents whole numbers.
y = 5.5  # Float data type: Represents numbers with decimal points.
name = "John"  # String data type: Represents text or a sequence of characters.

# Printing variables to the console
print("Integer:", x)
print("Float:", y)
print("String:", name)

# Step 3: List, Tuple, and Dictionary in Python
# Understanding different data structures in Python.

# A list is an ordered collection of items that can be changed (mutable).
fruits = ["apple", "banana", "orange"]
print("Fruits List:", fruits)

# A tuple is similar to a list but immutable (cannot be changed).
coordinates = (10, 20)
print("Coordinates Tuple:", coordinates)

# A dictionary stores data in key-value pairs.
person = {"name": "Alice", "age": 25}
print("Person Dictionary:", person)

# Step 4: Loading data using Pandas
# We load a dataset into a DataFrame, which is a 2D table-like data structure.

df = pd.read_csv("data.csv")  # Replace with your file path. This reads the CSV file into a DataFrame.
print("Data loaded from CSV:\n", df.head())  # Display the first 5 rows of the dataset.

# Step 5: Basic Data Operations with Pandas
# We perform some basic operations to explore and manipulate data.

# Display summary statistics of the dataset
print("\nSummary Statistics:\n", df.describe())  # Shows count, mean, std, min, max, etc.

# Filtering rows where 'age' is greater than 30
filtered_df = df[df['age'] > 30]
print("\nFiltered Data (Age > 30):\n", filtered_df)

# Handle missing values by filling them with the column mean
df['age'].fillna(df['age'].mean(), inplace=True)
print("\nData after filling missing values:\n", df.head())

# Step 6: Data Visualization with Matplotlib & Seaborn
# Visualization helps in understanding data patterns and relationships.

# Create a simple line plot using Matplotlib
plt.plot([1, 2, 3, 4], [10, 20, 25, 30])  # X values and Y values for the line plot.
plt.title("Simple Line Plot")  # Set a title for the plot.
plt.xlabel("X-axis")  # Label for the X-axis.
plt.ylabel("Y-axis")  # Label for the Y-axis.
plt.show()  # Display the plot.

# Create a histogram of the 'age' column using Seaborn
sns.histplot(df['age'], kde=True)  # kde=True adds a Kernel Density Estimate curve for smoother visualization.
plt.title("Age Distribution")  # Set title for the histogram plot.
plt.xlabel("Age")  # Label for the X-axis.
plt.ylabel("Frequency")  # Label for the Y-axis.
plt.show()  # Display the plot.

# Step 7: Numerical Operations with NumPy
# NumPy allows for efficient mathematical operations on arrays.

# Create a NumPy array with values 1, 2, 3, 4
arr = np.array([1, 2, 3, 4])
print("\nOriginal NumPy Array:", arr)

# Perform an element-wise operation on the array (square each value)
arr_squared = np.square(arr)  # Squaring each element in the array.
print("Squared NumPy Array:", arr_squared)

# Step 8: Introduction to Machine Learning with Scikit-learn
# We will create a simple machine learning model using the Scikit-learn library.

from sklearn.datasets import load_iris  # Load the famous Iris dataset.
from sklearn.model_selection import train_test_split  # For splitting the data into training and testing sets.
from sklearn.tree import DecisionTreeClassifier  # Decision tree classifier algorithm for classification tasks.
from sklearn.metrics import accuracy_score  # Function to evaluate the model's accuracy.

# Load the Iris dataset
data = load_iris()  # Loads the dataset into a dictionary-like structure.
X = data.data  # Features (input data), like petal length, petal width, etc.
y = data.target  # Labels (output data), representing the species.

# Split the data into training and testing sets
# 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Initialize the Decision Tree Classifier model
model = DecisionTreeClassifier()

# Train the model using the training data
model.fit(X_train, y_train)

# Make predictions on the test data
predictions = model.predict(X_test)

# Evaluate the accuracy of the model by comparing predicted vs actual labels
accuracy = accuracy_score(y_test, predictions)
print("\nModel Accuracy: {:.2f}".format(accuracy))  # Display accuracy as a percentage.

# Step 9: Conclusion and Next Steps
# Now that you understand the basics, you can begin exploring more advanced concepts in data science.

# You can try:
# 1. Experimenting with other machine learning models from Scikit-learn (e.g., RandomForest, SVM, etc.)
# 2. Exploring deep learning frameworks like TensorFlow and PyTorch for more complex tasks.
# 3. Diving into real-world datasets and solving problems like classification, regression, clustering, etc.

# This is just the beginning of your data science journey. Keep learning and experimenting with Python!


