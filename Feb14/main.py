from rectangleOrSquareCalculator import Rectangle, Square

cont = 'y'
while cont == 'y':
    choice = input('Rectangle or square? (r/s): ')
    if choice == 'r':
        height = int(input('Enter height: '))
        width = int(input('Enter width: '))
        new_rectangle = Rectangle(height, width)
        print(new_rectangle)
    else:
        height = int(input('Enter height: '))
        width = int(input('Enter width: '))
        new_square = Square(height, width)
        print(new_square)

    cont = input("Continue? (y/n): ")
print('Byes!')
