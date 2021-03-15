import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("food_choices.csv")

df.boxplot(column=["Gender","eating_out","employment","exercise","grade_level","on_off_campus","pay_meal_out","self_perception_weight","sports"],grid=False)

plt.show()