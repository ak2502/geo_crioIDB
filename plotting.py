import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("food_choices.csv")

df.boxplot(grid=False)

plt.show()