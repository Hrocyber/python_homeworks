# task5_13
# *Create a collection of 6 names inputed from console ,
# generate a new collection selecting only the names starting from ‘A’ and print it
col_names = []
while len(col_names) !=6:
 col_names.append(input())
print('col_names =', col_names)
new_col_numes = []
for word in col_names:
    if word[0] == "A":
        new_col_numes.append(word)
print('new_col_numes = ', new_col_numes )