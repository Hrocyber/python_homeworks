import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn import metrics
from sklearn import tree
import matplotlib.pyplot as plt

covid = pd.read_csv('effects_covid.csv')
# # print(alc)
# # print(alc.columns)
# # print(alc.isna().sum())
# # print(alc.shape)
# print(alc.tail(5))
# alc.info()
covid.fillna(covid.mean(), inplace=True)
# print('after fill \n ', alc.isna().sum())

le = LabelEncoder()

covid["Country"] = le.fit_transform(covid["Country"])
covid["Commodity"] = le.fit_transform(covid["Commodity"])
covid["Weekday"] = le.fit_transform(covid["Weekday"])
covid["Direction"] = le.fit_transform(covid["Direction"])

X = covid[['Value', 'Cumulative', 'Year', 'Commodity', 'Weekday', 'Country']]
y = covid['Direction']

covid.info()

# print(set(alc["Series_reference"]))
# Series_reference_encoded = le.fit_transform(alc["Series_reference"])
# print('Series_reference_encoded', Series_reference_encoded)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=50)

model = dtc(criterion="entropy", max_depth=1)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(set(covid['Direction']))
print("Accuracy:", metrics.accuracy_score(y_pred, y_test))

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(4, 4), dpi=266)

fn = ['Value', 'Cumulative', 'Year', 'Commodity', 'Country']
cn = ['right', 'left', 'center']

tree.plot_tree(model, feature_names=fn, class_names=cn, filled=True)

text_representation = tree.export_text(model)
print(text_representation)
covid.hist()
plt.show()
