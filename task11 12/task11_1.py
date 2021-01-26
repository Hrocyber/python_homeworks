# task11_1
# Create 2 processes:
# 1. calculate sum of list of numbers and print it;
# 2. calculate count of even elements in list of numbers and print it.
import multiprocessing
import functools

numbers = list(range(2000))


def addition(numbers):
    sum = functools.reduce(lambda num1, num2: num1 + num2, numbers)
    print('the sum =', sum)


def evencount(numbers):
    result = len(list(filter(lambda num: num % 2 == 0, numbers)))
    print('count of even elements = ', result)

if __name__ == "__main__":
    pr_1 = multiprocessing.Process(target=addition, args=(numbers,))
    pr_2 = multiprocessing.Process(target=evencount, args=(numbers,))
    pr_1.start()
    # pr_1.join()
    pr_2.start()
    # pr_2.join()
