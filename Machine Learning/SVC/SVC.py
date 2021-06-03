from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pandas as pd
banknot = pd.read_csv("bill_authentication.csv")
print(banknot.info())
print(banknot.isna().sum())



X = banknot.drop("Class", axis=1)
y = banknot["Class"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
# model = SVC(kernel="linear")
# model = SVC(kernel="poly", degree=8)
# model = SVC(kernel="sigmoid")
model = SVC(kernel="rbf")
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(classification_report(y_test,y_pred))
# print(confusion_matrix(y_test,y_pred))