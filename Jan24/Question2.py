def how_many(a_dict):
    total_length = 0
    for item in a_dict.values():
        total_length += len(item)
    return total_length


def main():
    animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
    animals['d'] = ['donkey']
    animals['d'].append('dog')
    animals['d'].append('dingo')
    print(how_many(animals))


if __name__ == '__main__':
    main()


