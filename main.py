import pandas as pd
import matplotlib.pyplot as plot
import seaborn as seaborn
import sklearn as sk
import sns as sns
from matplotlib import pyplot as plt

# Reading CSV (1.1)
print(f"{'-'*20} Question 1.1 {'-'*20}")
data = pd.read_csv('./data.csv')
dataframe = pd.DataFrame(data = data)

# Creating and printing summary (1.2)
print(f"{'-'*20} Question 1.2 {'-'*20}")
summary = pd.DataFrame.describe(data)
print(f'Data Summary:\n{summary}\n')

# Checking for Nulls (1.3)
print(f"{'-'*20} Question 1.3 {'-'*20}")
print(f'False for Nulls:\n{pd.DataFrame.notnull(data)}\n')
print(f'Sum of Nulls:\n{pd.DataFrame.isnull(data).sum()}\n')

# Replacing Nulls (1.3.a)
print(f"{'-'*20} Question 1.3(a) {'-'*20}")
print("Replacing Null Values. . . : \n")
data["Duration"].fillna(data["Duration"].mean(), inplace = True)
data["Pulse"].fillna(data["Pulse"].mean(), inplace = True)
data["Maxpulse"].fillna(data["Maxpulse"].mean(), inplace = True)
data["Calories"].fillna(data["Calories"].mean(), inplace = True)
print(f"Done!\n\nPrinting without Nulls:\n{pd.DataFrame.notnull(data)}")
print(f'Sum of Nulls:\n{pd.DataFrame.isnull(data).sum()}\n')

# Data Aggregation (1.4)
print(f"{'-'*20} Question 1.4 {'-'*20}")
print(f"Printing Duration Aggregated Stats:\n{summary['Duration']}\n")
print(f"Printing Max Pulse Aggregated Stats:\n{summary['Maxpulse']}\n")

# Filtering for Calories between 500 and 1000 (1.5)
print(f"{'-'*20} Question 1.5 {'-'*20}")
filtered = dataframe[dataframe['Calories'].between(500, 1000)]
print(f"Calories between 500 and 1000:\n{filtered}\n")

# Filtering for Calories above 500 and Pulse below 100 (1.6)
print(f"{'-'*20} Question 1.6 {'-'*20}")
filtered = dataframe.loc[(dataframe['Calories'] > 500) & (dataframe['Pulse'] < 100)]
print(f"Calories > 500 and Pulse < 100:\n{filtered}\n")

# Creating df_modified for all columns but Maxpulse (1.7)
print(f"{'-'*20} Question 1.7 {'-'*20}")
df_modified = dataframe.loc[:, data.columns != 'Maxpulse']
print(f"df_modified created without Maxpulse:\n{df_modified}\n")

# Removing Maxpulse from main dataframe (1.8)
print(f"{'-'*20} Question 1.8 {'-'*20}")
dataframe = dataframe.drop('Maxpulse', axis=1)
print(f"Maxpulse removed from dataframe:\n{dataframe}\n")

# Changing Calories to int datatype (1.9)
print(f"{'-'*20} Question 1.9 {'-'*20}")
dataframe = dataframe.astype({'Calories': 'int32'})
print(f"Changing Calories to int32 type:\n{dataframe['Calories']}\n")

# Create a scatter plot of duration and calories (1.10)
print(f"{'-'*20} Question 1.10 {'-'*20}")
scatter_plot = dataframe.plot.scatter(x='Duration', y='Calories')
plot.show()


