def main():
    card_dict = {'Wayne Gretzky': 2, 'Mario Lemieux': 3, 'Sidney Crosby': 1,
                 'Austin Mathews': 1, 'Jaromir Jagr': 2}
    purchased_hockey_cards = {"Wayne Gretzky": 1, "Alexander Ovechkin": 2, "Mark Messier": 2,
                              "Bobby Hull": 1}
    set1 = set(card_dict)
    set2 = set(purchased_hockey_cards)
    set1.update(set2)
    print(set1)


if __name__ == '__main__':
    main()