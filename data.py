import json  
import pandas as pd  
from pandas.io.json import json_normalize  
import requests
from tabulate import tabulate
from sklearn.cluster import KMeans
import random
import numpy as np
import pandas as pd

url = 'https://discover.search.hereapi.com/v1/discover?in=circle:19.1334,72.9133;r=5000&q=apartment&apiKey=uJHMEjeagmFGldXp661-pDMf4R-PxvWIu7I68UjYC5Q'
data = requests.get(url).json()
d=json_normalize(data['items'])

d2=d[['title','address.label','distance','access','position.lat','position.lng','address.postalCode','contacts','id']]

d.to_csv('apartment.csv')
d2.to_csv('cleaned_apartment.csv')

df_final=d2[['position.lat','position.lng']]

CafeList=[]
DepList=[]
GymList=[]
latitudes = list(d2['position.lat'])
longitudes = list( d2['position.lng'])
for lat, lng in zip(latitudes, longitudes):    
    radius = '1000' #Set the radius to 500 metres
    latitude=lat
    longitude=lng
    
    search_query = 'cafe' #Search for any cafes
    url = 'https://discover.search.hereapi.com/v1/discover?in=circle:{},{};r={}&q={}&apiKey=uJHMEjeagmFGldXp661-pDMf4R-PxvWIu7I68UjYC5Q'.format(latitude, longitude, radius, search_query)
    results = requests.get(url).json()
    venues=json_normalize(results['items'])
    CafeList.append(venues['title'].count())
	
    search_query = 'gym' #Search for any gyms
    url = 'https://discover.search.hereapi.com/v1/discover?in=circle:{},{};r={}&q={}&apiKey=uJHMEjeagmFGldXp661-pDMf4R-PxvWIu7I68UjYC5Q'.format(latitude, longitude, radius, search_query)
    results = requests.get(url).json()
    venues=json_normalize(results['items'])
    GymList.append(venues['title'].count())

    search_query = 'department-store' #search for supermarkets
    url = 'https://discover.search.hereapi.com/v1/discover?in=circle:{},{};r={}&q={}&apiKey=uJHMEjeagmFGldXp661-pDMf4R-PxvWIu7I68UjYC5Q'.format(latitude, longitude, radius, search_query)
    results = requests.get(url).json()
    venues=json_normalize(results['items'])
    DepList.append(venues['title'].count())

df_final['Cafes'] = CafeList
df_final['Department Stores'] = DepList
df_final['Gyms'] = GymList

print(tabulate(df_final,headers='keys',tablefmt='github'))

kclusters = 3

# run k-means clustering
kmeans = KMeans(n_clusters=kclusters, random_state=0).fit(df_final)
df_final['Cluster']=kmeans.labels_
df_final['Cluster']=df_final['Cluster'].apply(str)

print(tabulate(df_final,headers='keys',tablefmt='github'))