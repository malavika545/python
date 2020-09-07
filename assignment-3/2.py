'''2.	Draw correlation graph for mobile price with all attributes.'''
import pandas as pd
import matplotlib as plt
plt.rcParams.update({'figure.max_open_warning': 0})
df = pd.read_csv("mobile_cleaned-1549119762886.csv")
for col in df.columns:
    if(col != 'price'):
        df.plot(x='price',y=col)