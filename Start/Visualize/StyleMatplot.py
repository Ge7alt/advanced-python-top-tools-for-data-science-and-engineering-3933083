# Example file for Advanced Python: Top Tools for Data Science
# Using the Polars library create and access a DataFrame

import matplotlib.pyplot as plt
import pandas as pd

# Create a dataset for sales data
data = {
    'Month': ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    'SalesAmount': [1200, 800, 1400, 1500, 1900, 1500, 1300, 850, 1125, 1094, 1356, 1289],
    'Profits': [400, 200, 500, 300, -100, -200, 400, 500, 600, 450, 425, 525]
}

# Create a DataFrame from the data object
df = pd.DataFrame(data)

# Create a figure and axes 
fig, ax = plt.subplots()

# Set the chart title and labels
ax.set_title("Dow Jones Stock Values")
ax.set_xlabel("Date")
ax.set_ylabel("Value")

# Add the data series


# Add a legend to the chart


# Set line styles

plt.show()
