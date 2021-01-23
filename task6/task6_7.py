# task6_7
# *Calculate multiplication of numbers from 0 to inputed value and print it
number = int(input('please input the number \n'))
multipication = 1
while number > 1:
    multipication *= number
    number = number - 1
print('multiplication of numbers from 0 to inputed value = ', multipication)
