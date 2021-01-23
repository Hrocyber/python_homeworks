# task6_6
# *Define collection of prices, calculate their sum until meeting negative price
col = [1000, 2500, 2400, 4510, -140, -154, 452, -658]
prices = 0
for price in col:
    if price > 0:
        prices += price
print('sum of positive prices is ', prices)
