# task8_1
# Define some collection of names and get the collection of their first
# 3 characters using map(), print the result
col_names = ['Hrayr', 'Tigran', 'Tatevik', 'Levon', 'Arina']
new_list = list(map(lambda name: name[:3], col_names))
print(new_list)
