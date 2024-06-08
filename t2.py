import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (assuming it's a CSV file named 'sales_data.csv')
df = pd.read_csv('sales_data.csv')

# Display the first few rows of the dataframe
print("First few rows of the dataset:")
print(df.head())

# Data exploration tasks
# Filtering data
filtered_data = df[df['region'] == 'North']

# Sorting data
sorted_data = df.sort_values(by='sales', ascending=False)

# Grouping data
grouped_data = df.groupby('category')['sales'].sum()

# Summary statistics
mean_sales = df['sales'].mean()
median_sales = df['sales'].median()
std_dev_sales = df['sales'].std()

print("\nSummary Statistics:")
print("Mean Sales:", mean_sales)
print("Median Sales:", median_sales)
print("Standard Deviation of Sales:", std_dev_sales)

# Visualizing data distributions and relationships
# Distribution plot
plt.figure(figsize=(10, 6))
sns.histplot(df['sales'], kde=True)
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

# Relationship plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sales', y='profit', data=df, hue='category')
plt.title('Relationship between Sales and Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.show()
