#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

df = pd.read_csv(r'C:\projectgen\questionone.csv')
print (df)

mylabels = [df.countryregioncode]
myexplode = [0.1, 0, 0, 0, 0, 0]
total = sum(df.countrytotalsales)

plt.pie(df.countrytotalsales,  explode = myexplode, autopct='%1.2f%%')

plt.legend(title = 'Country Regional Code', labels = df.countryregioncode, bbox_to_anchor = (1.05, 1), loc= 'upper left')

plt.title('Regional Sales')
plt.show()

