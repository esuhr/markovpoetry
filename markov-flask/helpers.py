import re
from collections import defaultdict
from random import choice

def create_corpus(poems):
    text = '\n'.join(poems)
    words = text.split(' ')
    transition = defaultdict(words)

    return words, transition

def shortgenerator(words, transition, start_word):
    if start_word not in words:
        return None
    
    for w0, w1, w2 in zip(words[0:], words[1:], words[2:]):
        transition[(w0, w1)].append(w2)

    i = words.index(start_word)
    w0, w1, w2 = words[i : i + 3]

    newwords = []
    for _ in range(5):
        w0, w1, w2 = w1, w2, choice(transition[w1, w2])
        newwords.append(w2)

    return ' '.join(newwords)

def longgenerator(words, transition, start_word, num=100):
    if start_word not in words:
        return None
    
    for w0, w1, w2 in zip(words[0:], words[1:], words[2:]):
        transition[(w0, w1)].append(w2)

    i = words.index(start_word)
    w0, w1, w2 = words[i : i + 3]

    newwords = []
    for _ in range(num):
        w0, w1, w2 = w1, w2, choice(transition[w1, w2])
        newwords.append(w2)

    return ' '.join(newwords)