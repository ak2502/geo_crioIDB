import numpy as np 
import pandas as pd 

df = pd.read_csv("food_coded.csv")

df1=df[["GPA","Gender","eating_out","employment","exercise","grade_level","on_off_campus","pay_meal_out","self_perception_weight","sports"]]

df1.to_csv("food_choices.csv")
