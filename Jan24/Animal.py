animals = {'a': 'aardvark','b': 'baboon','c': 'coati'}
animals['d'] = 'donkey'

print(animals)
print(animals['c'])
# print(animals['donkey'])
print(len(animals))
animals['a'] = 'anteater'
print(animals['a'])
print(len(animals['a'])) # print the length of word of animal['a'] is anteater: 8
print('baboon' in animals)
print('donkey'in animals.values())
print('b'in animals)
print(animals.keys())
del animals['b']
print(len(animals))
print(animals.values())