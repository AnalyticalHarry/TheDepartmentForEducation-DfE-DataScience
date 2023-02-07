import pandas as pd

#Read data stored in 'balance,txt into a  DataFrame
df = pd.read_csv('balance.txt', delim_whitespace=True)

#Notice how we can use the mean() function to find average values.
print("The avereage income of a female is ", df[df.Gender == "Female"].loc[:,"Income"].mean())
print("The avereage income of a male is ",df[df.Gender == "Male"].loc[:,"Income"].mean())

# Notice how we use the groupby() function below.
# Find out more about the groupby function here: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby
print(df.groupby(['Gender']).mean())

print("The avereage age of people in our dataset is ",df.loc[:, "Age"].mean())

#Besides finding average values we can also find max and min values.
# mean(), min() and max() are all methods for computing descriptive statistics.
# Find more of these types of methods here: http://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html#descriptive-statistics
print("The youngest person in our dataset is ",df.loc[:, "Age"].min())
print("The oldest person in our dataset is ",df.loc[:, "Age"].max())
