# Example file for Advanced Python: Top Tools for Data Science
# Using the Polars library create and access a DataFrame

import matplotlib.pyplot as plt
import pandas as pd

# Read the stock data into a Pandas dataframe and then select the first 31 values
stockdata = pd.read_csv("HistoricalPrices.csv")
stockdata = stockdata.iloc[:31]

# Create a figure and axes 
fig, ax = plt.subplots()

# Set the chart title and labels
ax.set_title("Dow Jones Stock Values")
ax.set_xlabel("Date")
ax.set_ylabel("Value")

# Add the data series
ax.plot(stockdata["Date"], stockdata["Close"], color="blue")
ax.plot(stockdata["Date"], stockdata["Low"], color = "red")
ax.plot(stockdata["Date"], stockdata["High"], color = "green")

# Add a legend to the chart
ax.legend(["Close","Low","High"],loc='upper left')

# Set line styles

plt.show()
