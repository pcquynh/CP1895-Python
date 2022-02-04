from shapes import Circle, Rectangle
from scence import Scene
import pickle

def display_menu():
    print("Menu:")
    print("1: Save a scence")
    print("2: Load a scence")
    print("3: Create a new scence")
    print("4: Add circle to scence")
    print("5: Add rectangle to scence")
    print("6: Exit")


def save_scence(scence):
    with open("scence.bin", "wb") as file:
        pickle.dump(scence,file)


def load_scence(scence):
    with open("scence.bin", "rb") as file:
        print(pickle.load(file))


def create_scence():
    new_scence = Scene([])
    return new_scence


def add_circle_scence(scence):
    radius = float(input("Enter radius: "))
    new_circle = Circle(radius)
    scence.add_shapes(new_circle)


def add_rectangle_scence(scence):
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    new_rect = Rectangle(length, width)
    scence.add_shapes(new_rect)


def main():
    scence = create_scence()
    while True:
        option = int(input("Enter your choice: "))
        if option == 1:
            save_scence(scence)
        elif option == 2:
            load_scence(scence)
        elif option == 3:
            create_scence()
        elif option == 4:
            add_circle_scence(scence)
        elif option == 5:
            add_rectangle_scence(scence)
        elif option == 6:
            print("Bye!")
            break
        else:
            print("Invalid option")
            break


if __name__ == '__main__':
    main()