# task5_15
# Define a collection of pets, that stores types of pet and its name,
# find how many pets have name Johny and print the number

pet_col = {'cat': 'Artur', 'dog': 'Martin', 'snake': 'Johny', 'elephant': 'Mark', 'horse': 'Kety', 'cow': 'Johny'}
count = 0
for name in pet_col.values():
    if name == 'Johny':
        count += 1
print('count =', count)
