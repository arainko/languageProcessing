# This is a sample Python script.
import nltk
from nltk.book import *
from tabulate import tabulate


def lexical_diversity(text):
    return len(text) / len(set(text))


def flatten(_list):
    flattened = []
    for nestedList in _list:
        flattened.extend(nestedList)
    return flattened


def vocab_size(text):
    return len(set(text))


def max_length_word(text):
    return max(len(word) for word in set(text))


if __name__ == '__main__':
    print(len(text3))
    print(len(set(text3)))
    print(text1.count("monstrous"))
    print(text1.similar("monstrous"))
    print(text1.common_contexts(["stories", "pictures"]))
    # zadanie 1
    print('=' * 20)
    text1.common_contexts(["many", "dish"])
    text2.common_contexts(["lot", "woman"])
    text3.common_contexts(["dead", "bird"])
    text4.common_contexts(["lexical", "musical"])
    text5.common_contexts(["woman", "man"])
    text6.common_contexts(["letter", "love"])
    text7.common_contexts(["absence", "descent"])
    text8.common_contexts(["upper", "ascend"])
    text9.common_contexts(["supper", "man"])
    print('=' * 20)
    # zadanie 2
    table = [
        ["tekst", "liczba slow", "slowa rozne", "lexical_diversity"],
        ["text1", len(text1), len(set(text1)), lexical_diversity(text1)],
        ["text2", len(text2), len(set(text2)), lexical_diversity(text2)],
        ["text3", len(text3), len(set(text3)), lexical_diversity(text3)],
        ["text4", len(text4), len(set(text4)), lexical_diversity(text4)],
        ["text5", len(text5), len(set(text5)), lexical_diversity(text5)],
    ]
    print(tabulate(table))
    # zadanie 3
    fours = [word for word in text1 if len(word) == 4]
    print("4 literowe slowa: " + str(len(fours)))
    # zadanie 4
    moreThanSeventeen = [word for word in text1 if len(word) > 17]
    # zadanie 5
    texts = [sent1, sent2, sent3, sent4, sent5, sent6, sent7, sent8, sent9]
    dictForEach = [sorted(set(text)) for text in texts]
    uniqueDict = set(flatten(dictForEach))
    print(uniqueDict)
    # zadanie 6
    vocabSizeForEach = map(
        lambda text: vocab_size(text),
        [text1, text2, text3, text4, text5, text6, text7, text8, text9]
    )
    print(list(vocabSizeForEach))
    # zadanie 7
    print(FreqDist(text1).most_common(10))
    # zadanie 8
    # tu nie jestem pewien czy chciała pani wszystkie najdłuższe słowa czy tylko po jednym z każdego z tekstów
    # wystarczy, tutaj wersja dla jednego z każdego.
    textsToCheck = [text1, text2, text3, text4, text5, text6]
    wordSets = map(lambda text: set(text), textsToCheck)
    wordsWithLengths = map(lambda text: map(lambda word: (word, len(word)), text), wordSets)
    wordsWithLengthsDict = map(lambda text: dict(text), wordsWithLengths)
    maxLenWords = map(lambda voc: max(voc, key=lambda key: voc[key]), wordsWithLengthsDict)
    print(list(maxLenWords))
