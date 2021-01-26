# task8_5
# *Calculate subtraction of numbers collection using reduce.
import functools
col_numbers = [5, 6, 9, 8, 4, 7, 11, 2, 36, 5, 74]
subtraction = functools.reduce(lambda num1, num2: num1 - num2, col_numbers)
print('subtraction = ', subtraction)
