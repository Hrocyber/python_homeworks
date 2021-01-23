# task5_17
# *Create a collection of students with their scores and input them from console,
#  remove students with score less than 40 and print final collection
students_scores = {'Hrayr': 94, 'Armen': 78, 'Hasmik': 87, 'Gevorg': 37, 'Arsen': 57, 'Vardan': 39}
while len(students_scores) < 7:
    students_scores[input("please input score\n")] = input('please input name\n')
for unit in students_scores.items():
    if int(unit[1]) < 40:
        students_scores.pop(unit[0])
print(students_scores)
