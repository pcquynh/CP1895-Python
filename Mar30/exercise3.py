from dataStructure import Queue


def get_in_line(customer_queue):
    name = input("Please enter your name to be added to the line: ")
    customer_queue.enqueue(name)


def process_customer(customer_queue):
    if customer_queue.size() > 0:
        name = customer_queue.dequeue()
        print("Congratulation " + name + " Enjoy your new console")
    else:
        print("No customer in line")


def main():
    customer_queue = Queue()
    while True:
        print("Enter your selection: ")
        print("1. Get in line ")
        print("2. Process customer ")
        print("3. Exit ")

        selection = input("")
        if selection == "1":
            get_in_line(customer_queue)
        elif selection == "2":
            process_customer(customer_queue)
        elif selection == "3":
            break
        else:
            print("Invalid option")
    print("Bye!")


if __name__ == '__main__':
    main()