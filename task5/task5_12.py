# task5_12
# Define a collection of numbers, generate a new collection selecting only odd or dividable by 6 numbers and print it
col_numbers = [1, 5, 8, 7, 14, 12, 41, 18, 6, 24, 25, -17, -36]
new_col_numbers = []
for num in col_numbers:
    if num % 2 !=0 or num % 6 == 0:
        new_col_numbers.append(num)
print(new_col_numbers)