# CRIM - per capita crime rate by town
# ZN - proportion of residential land zoned for lots over 25,000 sq.ft.
# INDUS - proportion of non-retail business acres per town.
# CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)
# NOX - nitric oxides concentration (parts per 10 million)
# RM - average number of rooms per dwelling
# AGE - proportion of owner-occupied units built prior to 1940
# DIS - weighted distances to five Boston employment centres
# RAD - index of accessibility to radial highways
# TAX - full-value property-tax rate per $10,000
# PTRATIO - pupil-teacher ratio by town
# B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
# LSTAT - % lower status of the population
# MEDV - Median value of owner-occupied homes in $1000's


import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt


boston = pd.read_csv("Boston.csv")
# print(boston.info())
# print(boston.columns)
# print(boston.isna().sum())
X = boston[['crim', 'tax', 'rm']]
y = boston['chas']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100, stratify=y)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))
plt.matshow(boston.corr())
plt.xticks(range(boston.shape[1]), boston.columns, fontsize = 12, rotation =90)
plt.yticks(range(boston.shape[1]), boston.columns, fontsize = 12, rotation =0)
color_bar = plt.colorbar()
color_bar.ax.tick_params(labelsize =12)
plt.title('boston data')
boston.hist()
plt.show()