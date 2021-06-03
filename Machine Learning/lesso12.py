import pandas as pd
from sklearn.model_selection import  train_test_split
countries = pd.read_csv('us-counties.csv')
# print(countries.columns)
# print(countries.describe)
# print(countries.info)
print(countries.head(17))

X = countries[['date', 'fips']]
y = countries['deaths']

countries['fips'].fillna(value=1, inplace=True)
countries['fips'].fillna(value=1, inplace=True)

# print(help(countries.fillna))

# print(X.isna().sum())
# print('X', X.info())
# print('y', y.info())

X_train, X_test, y_traain, y_test = train_test_split(X, y, test_size=0.2, random_state=50, stratify=y)

