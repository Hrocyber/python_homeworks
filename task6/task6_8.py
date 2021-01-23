# task6_9
# Input collection of numbers, find last number which square root is less than 26, print it
col = [354, 654, 148, 784, 9654, 4542, 147, 588, 141, 987, 1541447]
list = []
for num in col:
    if pow(num, 0.5) < 26:
        list.append(num)
print('last number which square root is less than 26 in collection is ', list[-1])
