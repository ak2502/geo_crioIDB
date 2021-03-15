import numpy as np 
import pandas as pd 

df = pd.read_csv("food_coded.csv")

df1=df[["cook","diet_current_coded","eating_out","employment","exercise","fav_cuisine_coded","on_off_campus","pay_meal_out","fav_food","fruit_day","income"]]

df1.to_csv("food_choices.csv")
#print(df1)