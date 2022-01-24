# create a dictionary: 'key': value
Q_dictionary = {
    'first_name': 'Quynh',
    'last_name': 'Pham',
    'age': 33,
    'NetWorth': 500.56,
    'Vaccinated': True
}

# print dictionary
print(Q_dictionary)

# access a single value using the key
print(Q_dictionary['age'])

# how to change a value in a dictionary
Q_dictionary['age'] = 20
print(Q_dictionary)

# how to add a new element to a dictionary
Q_dictionary['nationality'] = 'Vietnamese'
print(Q_dictionary)

# delete
del Q_dictionary['NetWorth']
print(Q_dictionary)

country = Q_dictionary.get('country', 'cannot find this key')
print(country)

print(Q_dictionary.keys())

for code, value in Q_dictionary.items():
    print(code, value)
    print(f"{code} : {value}")


# convert a library to a list, sort the list, print the key and correspondent value
Q_list = list(Q_dictionary.keys())
Q_list.sort()
print(Q_list)
for small in Q_list:
    print(f"{small} : {Q_dictionary[small]}")