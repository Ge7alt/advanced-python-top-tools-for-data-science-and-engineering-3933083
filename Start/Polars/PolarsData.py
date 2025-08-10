# Example file for Advanced Python: Top Tools for Data Science
# Using the Polars library to manipulate data within a DataFrame

import polars as pl


df = pl.read_csv("sales_data.csv")


# 1. Sorting data
# sorted_df = df.sort('SalesAmount', descending=True)
# print(sorted_df)

# multi_sort = df.sort(['Product', 'SalesAmount'], descending=[True, True])

# 2. Filtering data
filtered_df = df.filter(pl.col('Region')=='North')
print(filtered_df)

# mean_val = pl.col("SalesAmount").mean()
# filtered = df.filter(pl.col("SalesAmount") > mean_val)
# print(filtered)

# 3. Use SQL to query the DataFrame directly within Polars
# amount = 850
# result = df.sql(
#   f"""
#   SELECT Product, SalesAmount
#   FROM self
#   Where SalesAmount > {amount}
#   """
# )
# print(result)
# 4. Grouping data and aggregation
result = df.group_by(pl.col("Product")).agg(
    pl.col("SalesAmount").sum().alias("Total Sales"),
    pl.col("SalesAmount").mean().alias("Average Sale"),
    pl.col("SalesAmount").max().alias("Largest Sale")
)
print(result)
