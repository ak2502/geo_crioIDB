import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("food_choices.csv")

df.boxplot(column=["cook","diet_current_coded","eating_out","employment","exercise","fav_cuisine_coded","on_off_campus","pay_meal_out","fav_food","fruit_day","income"],grid=False)

plt.show()