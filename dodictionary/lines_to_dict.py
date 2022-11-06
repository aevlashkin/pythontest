import re
from itertools import groupby

def lines_to_dict(text):
    dictionary=list()
    for string in text:
        dictionary+=string.split(" ")
    filtered = filter(lambda word: len(word) > 2, dictionary)
    dictionary = list(filtered)
    maped = map(lambda word: (re.sub("[^A-Za-z]", 
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

if __name__=='__main__':
    test()
