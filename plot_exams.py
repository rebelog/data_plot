import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("exames.csv")

#print(df.head())
#print(df.columns)
params = df.columns
#skip first 2 lines that store min and max values
date = df['date'][2:]

for param in params[1:]:
    data = df[param]
    #print(data)
    #print(data[1])
    min = float(data[0]) * np.ones(len(data)-2)
    max = float(data[1]) * np.ones(len(data)-2)
    y = data[2:]
        
    plt.plot(date, y, marker="o", color = "black")
    plt.plot(date, min, color = "blue", linestyle = ":")
    plt.plot(date, max, color = "red", linestyle = ":")
    plt.title(param)
    plt.show()    

