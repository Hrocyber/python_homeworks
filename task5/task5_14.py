# task5_14
# Define a collection of color names, generate a new collection selecting
# only color name having more than 1 ‘o’ and print it
col_colors = ['green', 'blue', 'red', 'brown', 'pink', 'white', 'black','yellow', 'ornage', 'borow', 'grey',
              'violet', 'colorific', 'colorful']
print(col_colors)
new_col_colors =[]
for color in col_colors:
    if color.count('o') > 1:
        new_col_colors.append(color)
print('new collection is ', new_col_colors)