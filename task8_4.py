# task8_4
# Create a collection of flowers with their color, get the flowers which color is red, print result
flowers = {'rose': 'red', 'mexak': 'white', 'kala': 'purple', 'kakach': 'red'}
red_flowers = list(filter(lambda x: flowers[x] == 'red', flowers))
print(red_flowers)
