# file handling
# text files, binary
with open("sample.txt", 'r') as filehandler:
    lines = filehandler.readlines()
    print(lines)

with open("sample.txt", 'a') as filehandler:
    data = input("Enter fruits: ")
    filehandler.write(data + "\n")

with open("sample.txt", 'r') as filehandler:
    lines = filehandler.readlines()
    print(lines)

