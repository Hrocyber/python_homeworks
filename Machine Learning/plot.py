import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

cars = ['BMW', 'AUDI', 'OPEL', 'SUZUKI', 'MERCEDES']
colors = ['green', 'red', 'white', 'pink', 'black']
years = [1999, 2010, 2020, 2007, 2014]
indexes = ['first', 'second', 'third', 'forth', 'fifth']
cars_seting = {'name': cars, 'color': colors, 'year': years}
cars_df = pd.DataFrame(cars_seting, index=indexes)
print(cars_df)
# print('erord toxn  ', cars_df.loc['third'], '\n')  # tpel toxn yst anuni
# print('chorord indexn ', cars_df.iloc[4])  # tpel toxn yst indexi
# print(cars_df.iloc[1:4])
# print(cars_df['year'].sum()) # konkret syunaki arjeqneri gumarn
print(cars_df.sum())  # amboxj faili arjeqneri gumarn yst syuneri
le = LabelEncoder()
cars_df['name'] = le.fit_transform(cars_df['name'])
cars_df['color'] = le.fit_transform(cars_df['color'])
cars_df.hist()

plt.scatter(cars, colors)

plt.matshow(cars_df.corr())  # corelaciai matric
plt.xticks(range(cars_df.shape[1]), cars_df.columns, fontsize=10, rotation=90)
plt.yticks(range(cars_df.shape[1]), cars_df.columns, fontsize=10)

color_bars = plt.colorbar()
color_bars.ax.tick_params(labelsize=12)
plt.title('Corelation matrix')
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(1000, 2000)
list1 = [4, 8, 9, 12, 45, 17, 19]
list2 = [24, 38, 49, 12, 45, 57, 59]
fig = plt.figure(figsize=(15, 15))
ax1 = fig.add_subplot(235)
ax2 = fig.add_subplot(233)
ax3 = fig.add_subplot(232)
ax4 = fig.add_subplot(236)
ax1.bar(list1, list2)
ax3.scatter(list2, list1, color='purple', linewidth=10)
ax2.hist(list1, color='pink')
ax2.set_title("histography")
ax4.plot(list1, list2, 'r^--')
ax2.set_xlim(10, 520)
plt.savefig("grafik.pdf")

plt.show()
