from lineslist_to_dict import lineslist_to_dict

in_file_path = 'book.txt'

in_text = 'null'
with open(in_file_path, 'r') as in_open_file:
    in_text = in_open_file.readlines()

dictionary = lineslist_to_dict(in_text)

print(dictionary)
print(len(dictionary))
