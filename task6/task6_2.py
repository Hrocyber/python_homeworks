# task6_3
# Create a collection for storing unique book names, add some of them from console and print results
col ={'A time to kill', 'The house of mirth', 'East of eden', 'The sun also rises', 'Vile bodies', 'A scanner darkly'}
while len(col) < 10:
    col.add(input('please input book name \n'))
print("the final collectin is", col)