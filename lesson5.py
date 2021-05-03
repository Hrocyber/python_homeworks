import pandas as pd
import matplotlib.pyplot as plt

names = ['Levon', 'Tatev', 'Arina', 'Sevak']
df = pd.DataFrame(names)
data = {'name': names, 'salary': [150, 600, 400, 450], 'gander': ['male', 'female', 'female', 'male'], 'age': [40, 22,
                                                                                                               45, 27]}
df_2 = pd.DataFrame(data, index=['admin', 'developer', 'manager', 'guard'])
print(df_2)
# print(df_2[['name', 'gander']])
# print(df_2.loc[['manager', 'admin']])
# print(df_2.iloc[[0, 2]])
# print(df_2.sum(axis=1))
# print(df_2['salary'].max())
# df_2.plot()
# df_2.plot.bar()
# plt.show()
df_3 = pd.read_csv('nba.csv')
# print(df_3.head())
# print(df_3.columns)
print(df_3['Weight'].mean())