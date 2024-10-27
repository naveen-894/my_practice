from operator import index
import numpy as np
import pandas as pd

# data = pd.Series([1, 2, 3, 4, 5,6])
# by default it uses index 
data = pd.Series([[1, 2, 3, 4, 5,6], [1,3]])
print(data)
data = pd.Series([[1, 2, 3, 4, 5,6], [1,3]], index=['hey', 'heyyy'])
print(data)
# hey      [1, 2, 3, 4, 5, 6]
# heyyy                [1, 3]

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}
df = pd.DataFrame(data)
print(df)
print('************')
age_column = df['Age']
print(age_column)
print('************', 'ageclear')
# Selecting rows using the `iloc` method (index-based selection)
first_row = df.iloc[0]
print(first_row)
print('************')
# Selecting rows using the `loc` method (label-based selection)
named_row = df.loc[1]  # Row with index label 1
print(named_row)


# df = pd.read_csv('data.csv')
# One way to deal with empty cells is to remove rows that contain empty cells.

# This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
new_df = df.dropna()

# The fillna() method allows us to replace empty cells with a value:
df.fillna(130, inplace = True)

# Replace NULL values in the "Calories" columns with the number 130:
# df["Calories"].fillna(130, inplace = True)

data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 22],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Default index (0-based, assigned automatically)
print(df)

df.set_index('Name', inplace=True)

# DataFrame with 'Name' as index
print(df)
print('*'*10)
# Using iloc to select the first row
print(df.iloc[0])
print('*'*10)
# Using loc to select the row with label 'John'
print(df.loc['John'])

"""
DataFrame Creation and Basic Operations:

Create a DataFrame with random data for 5 students containing their names, marks in Math, English, and Science.
Add a new column for the average of the three subjects.
Sort the DataFrame based on the average marks in descending order.
"""
data = {
    'name': ['naveen', 'raghu', 'srinath'],
    'maths_marks': np.random.randint(50, 100, 3),
    'science_marks': np.random.randint(50, 90, 3),
    'english_marks': np.random.randint(50, 80, 3)
}
df = pd.DataFrame(data)
# axis=1 tells pandas to perform the operation across columns within each row.
# axis=0 (the default) would perform the operation across rows within each column.
df['average'] = df[['maths_marks', 'science_marks', 'english_marks']].mean(axis=1)
print('*'*20)
sorted = df.sort_values(by='average', ascending=False)
print(df)
print(sorted)


"""
Indexing and Slicing:

Load a CSV file of your choice (e.g., weather data, stock prices) into a pandas DataFrame.
Display:
The first 5 rows.
A specific column (like "Temperature" or "Close price").
Rows from index 10 to 20.
Rows where a specific column's value is greater than a threshold.
"""

df = pd.read_csv('files/analysis-public-place-assaults-sexual-assaults-and-robberies-2015-csv.csv')
print(pd.options.display.max_rows)
print(df.head(15))
print(df[10:21])
threshold_value = 15
print(df[df['Region_2013_code']> threshold_value].head(15).sort_values(by='Region_2013_code'))

"""
GroupBy and Aggregation:

Create a DataFrame representing sales data with columns: Date, Store, Sales, and Product.
Group the data by Store and find:
The total sales for each store.
The average sales per store.
The maximum sale for each store.
Find the minimum sale for each store.
Calculate the total sales per product across all stores.
Find the average sales per product in each store.
Identify the store with the highest total sales.
Find the date with the highest sales in each store.
Determine how many sales entries each store has (i.e., count the transactions per store).
Calculate the percentage contribution of each store’s total sales to the overall total sales.
For each product, find the store with the highest and lowest average sales.
Identify which products have been sold in each store (unique products per store).
Calculate the cumulative sales per store over time (useful for seeing sales growth).
Group the data by both Store and Product, and find the total and average sales for each combination.
Calculate the monthly total sales per store (you can extract the month from the Date column and group by it).
Identify the product with the highest average sale across all stores.
Create a pivot table showing the total sales for each store-product combination.
Calculate the overall average sales for each store and see which days exceeded this average (to find high-performance days).
Determine the variance and standard deviation of sales per store to assess sales consistency.
"""
data = {
    'Date': ['2024-10-01', '2024-10-01', '2024-10-02', '2024-10-02', '2024-10-03', '2024-10-03'],
    'Store': ['Store A', 'Store B', 'Store A', 'Store B', 'Store A', 'Store B'],
    'Sales': [1500, 2000, 1600, 2100, 1700, 2200],
    'Product': ['Product 1', 'Product 1', 'Product 2', 'Product 2', 'Product 1', 'Product 2']
}
df = pd.DataFrame(data)
print(df.groupby('Store'))
print(df.groupby('Store')['Sales'].sum())
print(df.groupby('Store')['Sales'].mean())
print(df.groupby('Store')['Sales'].max())
# Find the minimum sale for each store.
print(df.groupby('Store')['Sales'].min())

# Calculate the total sales per product across all stores.
print(df.groupby('Product')['Sales'].sum())

# Find the average sales per product in each store.
print(df.groupby(['Product', 'Store'])['Sales'].mean())

# Calculate the total sales per product across all stores.
print(df.groupby('Product')['Sales'].sum())

# Identify the store with the highest total sales.
print(df.groupby('Product')['Sales'].sum().idxmax())
print(df.groupby('Product')['Sales'].sum().max())

# Determine how many sales entries each store has (i.e., count the transactions per store).
print(df.groupby('Store')['Sales'].count())
print(df.groupby('Store').count())

# For each product, find the store with the highest and lowest average sales.
print(df.groupby('Product')['Sales'].max())
print(df.groupby('Product')['Sales'].min())

"""
Handling Missing Data:

Create a DataFrame with some missing values (use NaN).
Use pandas to:
Identify missing values.
Fill missing values with the mean of the respective columns.
Drop rows with missing values.
"""

# Creating a DataFrame with missing values
data = {
    # 'Product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
    'Price': [100, np.nan, 150, 200, np.nan],
    'Quantity': [30, 20, np.nan, 15, 10],
    'Discount': [5, 10, np.nan, np.nan, 0]
}

df = pd.DataFrame(data)
print(df.isna())
print(df.isna().sum())
# for x in df:
#     df[x].fillna(df[x].mean(), inplace=True)

# Fill missing values with the mean of each numeric column without using inplace
df = df.apply(lambda x: x.fillna(x.mean()) if x.dtype in ['float64', 'int64'] else x)

df = df.dropna(subset=['Price', 'Discount'])
print(df)




# df.index = [f"Day-{x+1}" for x in df.index]
# for x in df.index:
#     print(type(df.loc[x]))


"""
Merging DataFrames:

Create two DataFrames:
One with employee IDs and their names.
Another with employee IDs and their salaries.
Merge these two DataFrames on the employee ID.
Find the average salary of all employees.
"""

# DataFrame with employee IDs and names
df_names = pd.DataFrame({
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
})

# DataFrame with employee IDs and salaries
df_salaries = pd.DataFrame({
    'EmployeeID': [101, 102, 103, 104, 106],
    'Salary': [70000, 80000, 75000, 90000, 60000]
})

df = pd.merge(df_names, df_salaries, on='EmployeeID', how='inner')
# df = pd.merge(df_names, df_salaries, on='EmployeeID', how='outer')
# df = pd.merge(df_names, df_salaries, on='EmployeeID', how='left')
# df = pd.merge(df_names, df_salaries, on='EmployeeID', how='right')
print(df['Salary'].mean())