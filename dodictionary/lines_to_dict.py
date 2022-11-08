import re
from itertools import groupby

def lines_to_dict(text):
    dictionary=list()
    for string in text:
        dictionary+=string.split(" ")
    return(filter_and_sort(dictionary))

def string_to_dict(string):
    dictionary=string.split(" ")
    return(filter_and_sort(dictionary))

def filter_and_sort(in_list):
    filtered = filter(lambda word: len(word) > 2, in_list)
    dictionary = list(filtered)
    maped = map(lambda word: (re.sub("[^A-Za-zА-Яа-яáéíñóúüÁÉÍÑÓÚÜ'\-]", 
                "", word)).lower(), dictionary)
    dictionary = list(maped)
    dictionary.sort()
    dictionary = [word for word, _ in groupby(dictionary)]
    dictionary.sort()
    return(dictionary)

def test():
    lines = list()
    lines.append('ltd is the function for') 
    lines.append('convert a list of string')
    lines.append('into a dictionary(list of words)')
    print(lines_to_dict(lines))

def test_string():
    text = 'я пишу какой-то текст в этой строке'
    print(string_to_dict(text))


if __name__=='__main__':
    test()
