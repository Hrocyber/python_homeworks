import  pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

df = pd.read_csv('Boston.csv')
# print(df.head())
# print(df.columns)
y = df['chas']
X = df[['crim', 'tax', 'lstat', 'indus']]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)

logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)
y_pred = logmodel.predict(X_test)
print(y_pred, y_test)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))