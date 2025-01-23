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

# Step 1: Importing the necessary libraries
# PyTorch and TensorFlow are two of the most widely used deep learning libraries.
# We'll start by importing both of these libraries and other necessary tools.

# PyTorch for deep learning models
import torch  # Core PyTorch library
import torch.nn as nn  # Neural network module
import torch.optim as optim  # Optimizers for training
from torch.utils.data import DataLoader, TensorDataset  # For loading and batching datasets

# TensorFlow for deep learning models
import tensorflow as tf  # Core TensorFlow library
from tensorflow.keras.models import Sequential  # Sequential model for building neural networks
from tensorflow.keras.layers import Dense  # Dense layer (fully connected layer)
from tensorflow.keras.optimizers import Adam  # Adam optimizer for training

# Step 2: Basic Tensor Operations with PyTorch
# PyTorch uses Tensors, which are multi-dimensional arrays similar to NumPy arrays.
# Let's start by creating and performing operations on tensors in PyTorch.

# Create a PyTorch tensor (like an array)
x = torch.tensor([1.0, 2.0, 3.0, 4.0])
print("\nPyTorch Tensor:", x)

# Perform basic operations (e.g., element-wise addition)
y = x + 2  # Adding 2 to each element of the tensor
print("Tensor after addition:", y)

# Step 3: Simple Neural Network with PyTorch
# Let's define a simple neural network using PyTorch.

# Define a simple feed-forward neural network with one hidden layer
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        # Define layers
        self.fc1 = nn.Linear(4, 3)  # First fully connected layer (input: 4, output: 3)
        self.fc2 = nn.Linear(3, 1)  # Second fully connected layer (input: 3, output: 1)
    
    def forward(self, x):
        # Define forward pass
        x = torch.relu(self.fc1(x))  # Apply ReLU activation to the output of the first layer
        x = self.fc2(x)  # Output layer
        return x

# Initialize the model
model = SimpleNN()
print("\nPyTorch Model Architecture:\n", model)

# Step 4: Training with PyTorch
# Now we will create a simple dataset, define a loss function and optimizer, and train the model.

# Example data (4 features and 1 label for simplicity)
data = torch.tensor([[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0]])
labels = torch.tensor([[10.0], [20.0]])

# Create a DataLoader for batching data
dataset = TensorDataset(data, labels)
train_loader = DataLoader(dataset, batch_size=2, shuffle=True)

# Define a loss function and optimizer
criterion = nn.MSELoss()  # Mean Squared Error loss function for regression
optimizer = optim.SGD(model.parameters(), lr=0.01)  # Stochastic Gradient Descent optimizer

# Training loop
for epoch in range(100):  # Train for 100 epochs
    for inputs, targets in train_loader:
        # Forward pass: compute predicted output by passing data to the model
        outputs = model(inputs)
        
        # Compute loss
        loss = criterion(outputs, targets)
        
        # Backward pass: compute gradients
        optimizer.zero_grad()  # Clear previous gradients
        loss.backward()  # Backpropagation
        optimizer.step()  # Update model parameters
    
    if epoch % 10 == 0:  # Print loss every 10 epochs
        print(f"Epoch {epoch+1}, Loss: {loss.item()}")

# Step 5: Basic Tensor Operations with TensorFlow
# Now let's switch to TensorFlow. We'll create a TensorFlow tensor and perform basic operations.

# Create a TensorFlow tensor
x_tf = tf.constant([1.0, 2.0, 3.0, 4.0])
print("\nTensorFlow Tensor:", x_tf)

# Perform basic operations (e.g., element-wise addition)
y_tf = x_tf + 2  # Adding 2 to each element of the tensor
print("Tensor after addition:", y_tf)

# Step 6: Simple Neural Network with TensorFlow
# Now let's define the same simple neural network model in TensorFlow.

# Define a simple neural network with one hidden layer using TensorFlow's Keras API
tf_model = Sequential([
    Dense(3, input_dim=4, activation='relu'),  # First hidden layer (input: 4, output: 3)
    Dense(1)  # Output layer (output: 1)
])

print("\nTensorFlow Model Architecture:\n", tf_model)

# Step 7: Training with TensorFlow
# Let's compile and train the model on the same dataset.

# Compile the model (define the loss function and optimizer)
tf_model.compile(optimizer=Adam(lr=0.01), loss='mse')

# Training the model
# We will use the same dataset and labels for simplicity
tf_model.fit(data.numpy(), labels.numpy(), epochs=100, batch_size=2)

# Step 8: Comparison of PyTorch and TensorFlow
# PyTorch and TensorFlow are both widely used, but there are a few key differences:
# - **PyTorch** uses dynamic computation graphs (eager execution), which makes it more flexible and easier to debug.
# - **TensorFlow** uses static computation graphs (by default), but with TensorFlow 2.0, it also supports eager execution.
# Both are capable of building and training deep learning models, and the choice between them often comes down to personal preference or specific use cases.

# Step 9: Conclusion and Next Steps
# Both PyTorch and TensorFlow have their strengths and can be used for various deep learning tasks, such as image classification, NLP, reinforcement learning, and more.
# As a beginner, you can start by experimenting with simple models and gradually move to more complex architectures.

# Next steps:
# 1. Try building different types of neural networks (CNNs, RNNs) using both PyTorch and TensorFlow.
# 2. Experiment with real-world datasets like MNIST, CIFAR-10, or IMDB for image and text classification tasks.
# 3. Learn about advanced deep learning topics like transfer learning, fine-tuning, and model deployment.




