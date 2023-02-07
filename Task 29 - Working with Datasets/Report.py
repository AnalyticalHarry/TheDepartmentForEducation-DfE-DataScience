import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('balance.txt',sep=' ')
    
    
#sum of error and missing values
df.isnull().sum()

#1. Compare average income base on Ethinicity
df["Ethnicity"].unique()
print(df.groupby('Ethnicity')['Income'].mean())

#2. On average, do married or single people made a higher balance?
print(df.groupby('Married')['Balance'].mean())

#3. What is the highest income in our dataset?
print(f"Highest income : {df['Income'].max()}")

#4.What is the lowest income in our dataset?
print(f"Lowest income : {df['Income'].min()}")

#5.How many cards do we have recorded in our dataset?
print(f"Total numbers of cards : {df['Cards'].sum()}")

#6.How many females do we have information for vs how many males?
sex = df["Gender"]
print(sex.value_counts())