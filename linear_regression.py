import pandas as pd
df = pd.read_csv('Boston.csv')
Y = df['tax']
X = df[['rm,', 'medv', 'nox']]
y_pred