# Data Source Link: https://archive.ics.uci.edu/dataset/186/wine+quality

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("D:\\Study\\03_Code_Projects\\DataSet_Repos\\wine+quality\\winequality-red.csv", sep=";")

print(df.head(n=10))
print('===' * 50)

print(df.info())
print('===' * 50)

print(df.describe())
print('===' * 50)

print(df.shape)
print('===' * 50)

print(df.columns)
print('===' * 50)

print(f"List of Unique values in Quality column: {df['quality'].unique()}")
print(f"Count of Unique values in Quality column: {len(df['quality'].unique())}")
print('===' * 50)

### Check for missing values in the dataset
print(df.isnull().sum())
print('===' * 50)

### Check for duplicate rescords in the dataset
print(df[df.duplicated()])
print('===' * 50)

### Remove the duplicate rescords from the dataset
df.drop_duplicates(inplace=True)
print(df.shape)
print('===' * 50)

### Check for correlation in the dataset
print(df.corr())
print('===' * 50)

### Visualize the correlation of the variables
# plt.figure(figsize=(12, 8))
# sns.heatmap(df.corr(), annot=True)
# plt.show()
# print('===' * 50)

### Vizualization
print(df['quality'].value_counts())
print("Conclusion: It is an imbalanced dataset")

# df['quality'].value_counts().plot(kind='bar')
# plt.xlabel("Wine Quality")
# plt.ylabel("Count")
# plt.show()
print('===' * 50)

### Check plot for every feature/attribute of teh dataset
# for column in df.columns:
#     sns.histplot(df[column], kde=True)
#     plt.show()
# print('===' * 50)

### Univariate, Bivariate, Multivariate ANalysis
# sns.pairplot(df)
# plt.show()
# print('===' * 50)

### Categorical plot
# sns.catplot(x='quality', y='alcohol', data=df, kind='box')
# plt.show()
# print('===' * 50)

### Scatter plot
sns.scatterplot(x='alcohol', y='pH', data=df, hue='quality')
plt.show()
print('===' * 50)

