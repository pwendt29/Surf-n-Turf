import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
city = input("Enter the city")

# charts average home price for the city entered over the past 8 years
def average_chart(filename):
    df = pd.read_csv(filename, usecols=[2, *range(5, 101)], index_col='RegionName')
    city_row = df.loc[f"{city}"]
    city_row.plot(title='Average housing cost over years')
    plt.xlabel('Time')
    plt.ylabel('Cost')
    plt.ticklabel_format(axis= 'y', style='plain')
    plt.show()

# most recent average price
def last_entry(filename, city):
    df = pd.read_csv(filename, usecols=[2, *range(5, 101)], index_col='RegionName')
    city_row = df.loc[f"{city}"]
    listed_data = city_row.tolist()
    print(listed_data[-1])


