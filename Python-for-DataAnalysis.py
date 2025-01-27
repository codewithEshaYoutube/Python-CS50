# NOTE:
# This script is best run in an interactive environment like:
# - Jupyter Notebook (https://jupyter.org/)
# - Google Colab (https://colab.research.google.com/)
# These platforms allow you to run code step-by-step, visualize plots, and explore datasets easily.
#
# To run the code in Google Colab or Jupyter Notebook:
# 1. Open the link (Google Colab or Jupyter Notebook).
# 2. Create a new Python notebook.
# 3. Copy-paste this entire code into a cell.
# 4. Run the cell by pressing Shift+Enter.
# Import necessary libraries for data analysis and visualization
import pandas as pd            # Pandas is used for data manipulation
import matplotlib.pyplot as plt # Matplotlib is used for creating visualizations
import seaborn as sns          # Seaborn is used for statistical visualizations

# Step 1: Load the 'tips' dataset from Seaborn library
# This dataset contains information about restaurant tips, such as total bill, tip, and customer details.
data = sns.load_dataset('tips')

# Step 2: Explore the dataset
# Check the first 5 rows of the dataset
print("First 5 Rows of Data:")
print(data.head())  # Displays the first 5 rows of the dataset

# Get basic information about the dataset (e.g., number of rows, column types, missing values)
print("\nDataset Information:")
print(data.info())

# Get summary statistics for numerical columns (mean, std, min, max, etc.)
print("\nSummary Statistics:")
print(data.describe())

# Step 3: Data Cleaning
# Check for missing values in the dataset
print("\nMissing Values in Each Column:")
print(data.isnull().sum())  # Counts the missing values in each column

# If we had missing values, we would handle them here (e.g., drop or fill them)
# Example of dropping rows with missing values:
# data_cleaned = data.dropna()
# Or filling missing values with a specific value (e.g., 0 or the mean of the column):
# data_filled = data.fillna(0)

# Step 4: Data Visualization - Histogram
# Let's create a histogram to visualize the distribution of the 'total_bill' column
plt.figure(figsize=(8, 6))  # Set the size of the plot
plt.hist(data['total_bill'], bins=20, color='skyblue', edgecolor='black')  # Create a histogram
plt.title('Distribution of Total Bill')  # Title of the plot
plt.xlabel('Total Bill ($)')  # Label for the x-axis
plt.ylabel('Frequency')  # Label for the y-axis
plt.show()  # Display the plot

# Step 5: Data Visualization - Boxplot
# Create a boxplot to visualize the distribution of total bill by the day of the week
plt.figure(figsize=(8, 6))
sns.boxplot(x='day', y='total_bill', data=data, palette='Set2')  # Create the boxplot
plt.title('Total Bill Distribution by Day')  # Title of the plot
plt.show()  # Display the plot

# Step 6: Data Visualization - Pairplot
# A pairplot helps in understanding relationships between multiple numerical columns
sns.pairplot(data)  # This will create a grid of plots to explore relationships between numerical columns
plt.show()  # Display the pairplot

# Step 7: Correlation Analysis
# A correlation matrix helps us understand the relationships between numerical variables
corr = data.corr()  # Compute the correlation matrix for numerical columns

# Let's visualize the correlation matrix using a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)  # Create the heatmap
plt.title('Correlation Heatmap')  # Title of the plot
plt.show()  # Display the heatmap

# Step 8: Advanced Visualization - Scatter Plot
# Let's create a scatter plot to see the relationship between 'total_bill' and 'tip'
plt.figure(figsize=(8, 6))
sns.scatterplot(x='total_bill', y='tip', data=data, color='purple')  # Scatter plot of total_bill vs tip
plt.title('Total Bill vs Tip')  # Title of the plot
plt.xlabel('Total Bill ($)')  # Label for the x-axis
plt.ylabel('Tip ($)')  # Label for the y-axis
plt.show()  # Display the scatter plot

# Step 9: Grouping Data and Aggregation
# Let's calculate the average total bill per day
average_bill_per_day = data.groupby('day')['total_bill'].mean()
print("\nAverage Total Bill Per Day:")
print(average_bill_per_day)  # Displays the average total bill for each day

# Step 10: Insights and Conclusions
# Example Insight: If you want to know the average tip given by males and females, you can do this:
average_tip_by_gender = data.groupby('sex')['tip'].mean()
print("\nAverage Tip by Gender:")
print(average_tip_by_gender)  # Displays the average tip for each gender

# You can expand the analysis by exploring other questions like:
# 1. The relationship between the size of the group ('size' column) and the total bill.
# 2. The differences in tipping behavior on different days or times of day.

# Example of a more complex analysis (e.g., calculating the average tip based on day and time):
average_tip_by_day_time = data.groupby(['day', 'time'])['tip'].mean()
print("\nAverage Tip by Day and Time:")
print(average_tip_by_day_time)  # Displays the average tip based on day and time of the day

