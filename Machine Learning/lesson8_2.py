import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt

df_train = pd.read_csv('mnist_train.csv', header=None)
# print(df_train.isna().sum())
# print('syuneri qanak', len(df_train.columns))
# print(df_train.shape)
df_test = pd.read_csv('mnist_test.csv', header=None)
# print(df_test.isna().sum())
# print(df_test.shape)
# print(df_train.iloc[:, 0].value_counts())
# sns.countplot(df_train.iloc[:, 0])
# plt.show()
X_train = df_train.iloc[:, 1:]
y_train = df_train.iloc[:, 0]
X_test = df_test.iloc[:, 1:]
y_test = df_test.iloc[:, 0]
print(X_train.iloc[0, :])
image1 = X_train.iloc[10015].values.reshape(28, 28)
plt.imshow(image1, cmap='BuGn')
plt.title(y_train.iloc[10015])
# plt.show()
print(X_train.iloc[10015, 0])
model = SVC(kernel='rbf')
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(metrics.accuracy_score(y_pred, y_test))
print(model.predict([X_train.iloc[10015]]))
