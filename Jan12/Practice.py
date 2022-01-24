# ask user to enter first name, last name, age
# store that info in a dict
# print that dict
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
new_dictionary = {}
new_dictionary['first_name'] = first_name
new_dictionary['last_name'] = last_name
new_dictionary['age'] = age
print(new_dictionary)

# allow user to update age
choice = input('Do you want to update age? (y/n): ')
if choice == 'y':
    new_dictionary['age'] = int(input('Update age: '))
print(new_dictionary)

