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

age_column = df['Age']
print(age_column)
print('************')
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