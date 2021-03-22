import numpy as np 
from tabulate import tabulate
import pandas as pd 
from sklearn.cluster import KMeans
import random
import seaborn as sns
import matplotlib.pyplot as plt 


#data cleaning and extracting relevant features
df1 = pd.read_csv("codebook_food/food_coded.csv")
df=df1[["cook","diet_current_coded","eating_out","sports","exercise","fav_cuisine_coded","on_off_campus","pay_meal_out","fav_food","fruit_day","income"]]
df.dropna(axis=0,inplace=True)
df.to_csv("codebook_food/food_choices.csv")

print(tabulate(df,headers = 'keys', tablefmt = 'psql'))


#Plotting Boxplot for cleaned data
sns.boxplot(data=df, palette="Set1").tick_params(labelsize=8.7)
plt.xticks(rotation=45, ha='right')
plt.show()


#K-Means clustering on cleaned data
k = 3
kmeans = KMeans(n_clusters = k, random_state=0).fit(df)
df['Cluster']=kmeans.labels_


#Plotting Boxplot for optimal K value (K=3)
fig, axes = plt.subplots(1, k, sharey=True)
axes[0].set_ylabel('Coded Values', fontsize=20)

for i in range(k):
     plt.sca(axes[i])
     plt.xticks(rotation=45,ha='right')
     sns.boxplot(palette="Set1",data = df[df['Cluster'] == i].drop('Cluster',1), ax=axes[i]).tick_params(labelsize=8.7)
        
plt.show()
