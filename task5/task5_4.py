# task5_4
# Input a string, print it from start to half if its length is even, otherwise from half to the end
str = input("please input a string \n")
half_str = len(str)//2
print(str[0:half_str]) if len(str) % 2 ==0 else print(str[half_str:])