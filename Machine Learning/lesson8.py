import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("Iris.csv")
# print(df.describe)
# print(df.info())
print(df.columns)
# print(df.isna().sum())
le = LabelEncoder()
df['Species'] = le.fit_transform(df['Species'])
y = df['Species']
X = df[['SepalWidthCm', 'PetalWidthCm', 'SepalLengthCm', 'PetalLengthCm']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)
model = SVC(kernel='poly', degree=4)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(metrics.accuracy_score(y_pred, y_test))
