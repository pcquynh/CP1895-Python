def add_card(card_dict):
    card_name = input("Please enter card to add: ")
    if card_name in card_dict:
        card_dict[card_name] += 1
    else:
        card_number = int(input("Please enter the number of card to add: "))
        card_dict[card_name] = card_number


def list_card(card_list):
    for card, number in card_list.items():
        print(f"{card} : {number}")


def remove_card(card_dict):
    card_name = input("Please enter card to remove: ")
    if card_name not in card_dict:
        print("Card not in the list")
    else:
        card_dict.pop('card_name')

def display_menu():
    print("1. Add card")
    print("2. List card")
    print("3. Remove card")
    print("4. Exit")


def main():
    card_dict = {'Wayne Gretzky': 2, 'Mario Lemieux': 3, 'Sidney Crosby': 1,
                 'Austin Mathews': 1, 'Jaromir Jagr': 2}

    while True:
        display_menu()
        option = input("Enter your option: ")
        if option == "1":
            add_card(card_dict)
        elif option == "2":
            list_card(card_dict)
        elif option == "3":
            remove_card(card_dict)
        elif option == "4":
            break
        else:
            print("Invalid option")

    print("Bye!")


if __name__ == '__main__':
    main()