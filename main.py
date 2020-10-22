# This is a sample Python script.
import nltk
from nltk.book import *
from tabulate import tabulate


def lexical_diversity(text):
    return len(text) / len(set(text))

def zad1():
    pass


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
    print("4 literowe slowa:" + str(len(fours)))
    # zadanie 4
    moreThanSeventeen = [word for word in text1 if len(word) > 17]
