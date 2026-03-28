import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# charts average home price for the city entered over the past 8 years
df = pd.read_csv('RealEstate.csv', usecols=[2, *range(5, 101)], index_col='RegionName')
city = input("Enter the city")
city_row = df.loc[f"{city}"]
city_row.plot(title='Average housing cost over years')
plt.xlabel('Time')
plt.ylabel('Cost')
plt.ticklabel_format(axis= 'y', style='plain')
plt.show()

