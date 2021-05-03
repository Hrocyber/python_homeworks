import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

df = pd.read_csv("train.csv")
# print(df.columns)
# print(df.head(18))
# print(df.tail(10))
# print(df.describe())
# print(df.isna().sum())
le = LabelEncoder()
df['Name'] = le.fit_transform(df['Name'])
df['Sex'] = le.fit_transform(df['Sex'])
df['Ticket'] = le.fit_transform(df['Ticket'])
df['Cabin'] = le.fit_transform(df['Cabin'])
df['Embarked'] = le.fit_transform(df['Embarked'])
# print(df["Age"])

df.fillna(df.mean(), inplace=True)
# # print('second',df.isna().sum())
# # df["Age"].fillna(df["Age"].mean(), inplase=True)
# print(df["Age"])
# print('bacakayox arjeqnern  lracneluc heto ', df.isna().sum())
X = df[["Sex", "Ticket", "Pclass", "Age"]]
model = KMeans(n_clusters=3, max_iter=100)
model.fit(X)
print(model.predict(X))