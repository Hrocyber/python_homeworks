# task5_16
# *Create a collection for storing hotel visitors (name, country), input several visitors from console,
# print how many visitors are now in hotel,
# what is their country, what is their name

visitors = {'Hrayr': 'Armenia', 'Jhon': 'USA', 'Milena': 'France', 'Angelina': 'Spain', 'Piter': 'Italy'}
while len(visitors) < 7:
    visitors[input("please input name\n")] = input('please input country\n')

print(visitors)
print('visitors count is ', len(visitors))