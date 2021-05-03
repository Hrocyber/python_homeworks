import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn import metrics
from sklearn import tree
import matplotlib.pyplot as plt

df = pd.read_csv('Iris.csv')
print(df.columns)
# print(df.isna().sum())
# print(df.shape)
# print(df.tail(5))
df.info()
le = LabelEncoder()
df['Species'] = le.fit_transform(df["Species"])

X = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm']]
y = df['Species']
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=109)
plt.matshow(X.corr())
plt.xticks(range(X.shape[1]), X.columns, fontsize=12, rotation=90)
plt.yticks(range(X.shape[1]), X.columns, fontsize=12)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=12)
plt.title('Correlation Matrix')
plt.show()

X.hist()
plt.show()

plt.bar(df['Species'].unique(), df['Species'].value_counts(), color=['red', 'blue', 'orange'])
plt.xticks([0, 1, 2])
plt.xlabel('Target Classes')
plt.ylabel('Count')
plt.title('Count of each Target Class')
plt.show()
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100)




# print(df["sex"].unique())
