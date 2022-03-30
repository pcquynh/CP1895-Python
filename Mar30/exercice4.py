from dataStructure import Stack


# def enter_character(character_stack):
#     while True:
#         char = input("Please enter character: ")
#         if char == "%":
#             break
#         else:
#             character_stack.push(char)
#
# def main():
#     character_stack = Stack()
#     enter_character(character_stack)
#     print_result = ""
#     for i in range(character_stack.size()):
#         print_result += character_stack.pop()
#     print(print_result)



def accept_input(letter_stack):
    key_input = input("Enter a letter")
    key_input = key_input[0]
    letter_stack.push(key_input)
    if key_input == "%":
        return False
    return True


def print_in_reverse(letter_stack):
    while letter_stack.size() > 0:
        current_letter = letter_stack.pop()
        print(current_letter)


def main():
    letter_stack = Stack()
    keep_going = True
    while keep_going:
        keep_going = accept_input(letter_stack)
    print_in_reverse(letter_stack)


if __name__ == '__main__':
    main()