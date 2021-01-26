# task8_2
# Input 2 collections of numbers, get the collection where each i-th element is square
# sum  of corresponding elements in that 2 collections, print result
col_num1 = [2, 9, 4, 7, 8, 5, 3, 6, 7, 5]
col_num2 = [6, 8, 5, 7, 6, 8, 5, 7, 5, 7]
new_col = list(map(lambda number1, number2: number1 ** 2 + number2 ** 2, col_num1, col_num2))
print(new_col)
