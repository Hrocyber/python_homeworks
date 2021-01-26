# task11_5
# *Input a collection of numbers, create 3 extra processes, one for adding 2 to each element,
# 2-nd for calculating number of positive elements in result of 1-st,
# 3-rd to calculate power 5 of result of 2-nd and print the result.

import multiprocessing

numbers = list(range(-72772, 7727))


def addingtwo(numbers, queue):
    numbers_1 = list(map(lambda num: num + 2, numbers))
    queue.put(numbers_1)
    print(numbers_1)


def count_pos_elements(queue):
    queue.get()
    numbers_2 = list(filter(lambda num_1: num_1 > 0, queue))
    len_numbers_2 = len(numbers_2)
    queue.put(len_numbers_2)
    print(len_numbers_2)


def power5(queue):
    print(queue.get() ** 5)


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    pr_1 = multiprocessing.Process(target=addingtwo, args=(numbers, queue))
    pr_2 = multiprocessing.Process(target=count_pos_elements, args=(queue,))
    pr_3 = multiprocessing.Process(target=power5, args=(queue,))
    pr_1.start()
    pr_1.join()
    pr_2.start()
    pr_2.join()
    pr_3.start()
    pr_3.join()
