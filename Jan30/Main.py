from Shapes import Circle, Rectangle
import pickle


def add_shapes(shapes):
    cont = "y"
    while cont == "y":
        choice = int(input("Create circle/ rectangle: 1. circle   2.rectangle: "))
        if choice == 1:
            radius = float(input("Enter radius: "))
            new_circle = Circle(radius)
            shapes.append(new_circle)
        else:
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            new_rect = Rectangle(length, width)
            shapes.append(new_rect)
        cont = input("Do you want to add more shapes?: (y/n)")


def save_shapes(shapes):
    with open("shapes.bin", "wb") as file:
        pickle.dump(shapes, file)


def load_shapes(shapes):
    with open("shapes.bin", "rb") as file:
        print(pickle.load(file))


def main():
    shapes = []
    add_shapes(shapes)
    save_shapes(shapes)
    load_shapes(shapes)


if __name__ == '__main__':
    main()