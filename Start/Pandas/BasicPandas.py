# Example file for Advanced Python: Top Tools for Data Science
# Using the Pandas library create and access a DataFrame


import pandas as pd

# Create a dataset for sales data
data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Laptop', 'Smartphone', 'Tablet', 'Laptop', 'Smartphone'],
    'Region': ['North', 'North', 'North', 'South', 'South', 'South', 'East', 'East'],
    'SalesAmount': [1200, 800, 400, 1500, 900, 500, 1300, 850],
    'Quarter': ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3'],
    'Year': [2025, 2025, 2025, 2025, 2025, 2025, 2025, 2025]
}

# 1. Create a DataFrame from the data object
df = pd.DataFrame(data)

# 2. Display the DataFrame
# print(df)

# 3. Using describe() and info()
# print(df.info())
# print(df.describe(include='all'))

# 4. Accessing specific columns
# print(df[['Product']])

# 5. Adding a new column for Discounted Sales (10% discount)
df['SalesEuros'] = df['SalesAmount'] * .936
# print(df)

# 6. Add a new row using the concat() function
new_row = pd.DataFrame({
    'Product': ["Laptop"],
    'Region': ["West"],
    'SalesAmount' : [1400],
    'Quarter' : ["Q4"],
    'Year': [2025]
})

df = pd.concat([df, new_row], ignore_index=True)
# print(df)

# 7. Use the loc[] and iloc[] accessors to select row ranges
print(df.loc[1:4]) # use loc when you know index label or boolean condition
print(df.iloc[1:4]) # use iloc when need to work with numerical positions regarless of the index values