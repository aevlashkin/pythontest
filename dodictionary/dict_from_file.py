from lines_to_dict import *


in_file_path = 'book.txt'
in_text = 'null'


def main():
    with open(in_file_path, 'r') as in_open_file:
        in_text = in_open_file.readlines()
    dictionary = lines_to_dict(in_text)
    print(dictionary)
    print(len(dictionary))

if __name__=='__main__':
    main()
