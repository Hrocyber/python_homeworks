# task6_4
# Create 2 collections for storing movies that have been watched by 2 persons,
# get movies that are watched by at least one of them,
# get movies that are watched by 1-st and not watched by 2-nd, print results
movies_1 = {'Aladdin', 'Akira', 'Albatros', 'Alexander', 'Troy', 'Big Fish', 'Blue Velvet', 'Chicago', 'Citizen Kane'}
movies_2 = {'Aladdin', 'Fantasia', 'Fargo', 'Halloween', 'Hannibal', 'Hero', 'Troy', 'Hulk', 'Ice Princess'}
print('movies that are watched by at least one of them are\n', movies_1 | movies_2, '\n')
print('movies that are watched by 1-st and not watched by 2-nd\n', movies_1 - movies_2)
