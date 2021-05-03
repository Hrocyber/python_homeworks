import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn import metrics
from sklearn import tree
import matplotlib.pyplot as plt
diab = pd.read_csv('diabetes.csv')
# print(diab)
# print(diab.columns)
# print(diab.isna().sum())
# print(diab.shape)
# print(diab.tail(5))
X = diab[['plas', 'insu', 'mass']]
y = diab['class']
le = LabelEncoder()
y = le.fit_transform(y)
# print(y)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=109)

model = dtc(criterion="gini", max_depth=1)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_pred, y_test))

fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=100)

fn=['plas', 'insu', 'mass']
cn=['possitive', 'negative']

tree.plot_tree(model,feature_names = fn,class_names=cn,filled = True, );
plt.show()
text_representation = tree.export_text(model)
print(text_representation)