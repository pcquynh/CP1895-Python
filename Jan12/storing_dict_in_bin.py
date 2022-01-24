import pickle
Q_dictionary = {
    'first_name': 'Quynh',
    'last_name': 'Pham',
    'age': 33,
    'NetWorth': 500.56,
    'Vaccinated': True
}
with open("dictionary.bin", "wb") as file:
    pickle.dump(Q_dictionary, file)

with open('dictionary.bin', 'rb') as file:
    print(pickle.load(file))
