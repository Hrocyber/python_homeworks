import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

df = pd.read_excel('car_data.xlsx')
print(df.columns)
# print(df.head(5))
# print(df.tail(3))
# print(df.shape)
le = LabelEncoder()
df['buying'] = le.fit_transform(df['buying'])
df['maint'] = le.fit_transform(df['maint'])
df['class'] = le.fit_transform(df['class'])
df['safety'] = le.fit_transform(df['safety'])
df['doors'] = le.fit_transform(df['doors'])
df['persons'] = le.fit_transform(df['persons'])
df['lug_boot'] = le.fit_transform(df['lug_boot'])

X = df[['buying', 'safety', 'lug_boot', 'persons']]
y = df['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=109)

model = GaussianNB()
model.fit(X_train, y_train)
predicted = model.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, predicted))
