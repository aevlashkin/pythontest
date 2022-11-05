import re
from itertools import groupby

def lineslist_to_dict(text):
    dictionary=list()
    for string in text:
        dictionary+=string.split(" ")
    filtered = filter(lambda word: len(word) > 2, dictionary)
    dictionary = list(filtered)
    maped = map(lambda word: (re.sub("[^A-Za-z]", "", word)).lower(), dictionary)
    dictionary = list(maped)
    dictionary.sort()
    dictionary = [word for word, _ in groupby(dictionary)]
    dictionary.sort()
    return(dictionary)
