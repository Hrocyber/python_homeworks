import numpy as np

numbers_list = [10, 45, 47, 48, 14]
# print(numbers_list)
numbers_numpy = np.array(numbers_list)  # list to numpy array
# print(numbers_numpy)
random_array = np.random.rand(4, 5) * 10 + 1
# print(random_array)
# print(random_array[2, 3])
# print(random_array[1: 4, 4])
# print(random_array.sort())
array_zero = np.zeros((2, 3))
# print(array_zero)
array_certain_number = np.full((4, 5), 7)
# print(array_certain_number)
concatenate_arrays = np.concatenate((array_certain_number, random_array), axis=1)
print(concatenate_arrays)
print("minimum = ", concatenate_arrays.min())
print("minimums of colums = ", concatenate_arrays.min(axis=1)) # syan minimal arjeq@
print(np.split(concatenate_arrays, 2))

diabetes = np.genfromtxt("diabetes.csv", delimiter=",", skip_header=1)  # READ FROM CSV FILE
# print(diabetes)
new_csv = np.savetxt("new_text.csv", [4, 6, 7], delimiter=".")  # write in file