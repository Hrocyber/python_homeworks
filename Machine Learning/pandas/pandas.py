from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import LabelEncoder

usa = pd.read_csv("us-counties.csv")
print(usa.columns)  # tpel syunern
print("skzvic mi qani tox\n", usa.head(4))
# print("verjic mi qani tox\n", usa.tail(3))
# print(usa.describe())
# print(usa.info())
# print(usa.dtypes)
# print(usa['state'].dtypes)
# print(usa.iloc[1:3])  # tpel konkret mijakayqov toxer
# print(usa.shape) # toxeri u syuneri qanak
# print(usa["date"].head(2)) #konkret syan mijic skzbi arjeqner
# print(set(usa["county"])) # unikal arjeqner konkret syan

# print(usa.isna().sum())  # @ndhanur fayli mej bacakayox arjeqner
# print(usa["state"].isna().sum())  # konkret syan bacakayox arjeqner
# usa["fips"].fillna(usa["fips"].mean(),
#                    inplace=True)  # bacakayox arjeqnern lcnel henc ayd syan arjeqneri mijinacvac tverov
# usa["deaths"].fillna(usa["deaths"].mean(),
#                      inplace=True)  # bacakayox arjeqnern lcnel henc ayd syan arjeqneri mijinacvac tverov
# print(set(usa["county"]))  # unikal arjeqner konkret syan
# print(usa["fips"].isna().sum())  # konkret "fips" syan bacakayox arjeqner
# print(usa["deaths"].isna().sum())  # konkret "fips" syan bacakayox arjeqner
# usa.dropna() # bacakayox arjeq unecox syuneri jnjum
# print(usa[usa["fips"].notna()].shape) # voch zroyakan arjeqneri qanakn konkret syan
# le = LabelEncoder()
# usa.drop(["cases"]) # konkret syan jnjum
# usa["date"] = le.fit_transform(usa["date"])           #object to number
# usa["county"] = le.fit_transform(usa["county"])       #object to number
# usa["state"] = le.fit_transform(usa["state"])         #object to number
