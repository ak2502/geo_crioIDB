from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("food_coded.csv")
x = df[["weight","waffle_calories"]]


k = 8

Centroids = (x.sample(n = k))

plt.scatter(x["weight"],x["waffle_calories"],c ='b')
plt.scatter(Centroids["weight"],Centroids["waffle_calories"],c='red')


plt.xlabel("Weight")
plt.ylabel("Waffle Calories")
plt.show()