# This is a sample Python script.
import nltk
import re
from nltk.book import *
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plot
from tabulate import tabulate

texts = [text1, text2, text3, text4, text5, text6, text7, text8, text9]


def newline():
    print("\n")


def different_bigrams():
    _bigrams = list(nltk.bigrams(text5))
    distinct_bigrams = len(set(_bigrams))
    most_common_bigrams = Counter(_bigrams).most_common(10)
    most_common_words = FreqDist(text5).most_common(10)
    print("There are " + str(distinct_bigrams) + " distinct bigrams")
    print("10 most common bigrams: " + str(most_common_bigrams))
    print("10 most common words: " + str(most_common_words))


def ngrams():
    _ngrams = map(lambda n: (n, len(list(nltk.ngrams(text5, n)))), range(3, 7))
    return list(_ngrams)


def ngram_graph():
    stringified_ngrams = map(lambda ntuple: (str(ntuple[0]), ntuple[1]), ngrams())
    ngram_dict = dict(stringified_ngrams)

    plot.bar(range(len(ngram_dict)), list(ngram_dict.values()), align='center')
    plot.xticks(range(len(ngram_dict)), list(ngram_dict.keys()))
    plot.xlabel('n-gram degree', fontsize=8)
    plot.ylabel('n-gram count', fontsize=8)
    plot.show()


def words_ending_with_ing():
    return [word for word in text1.tokens if re.search(r'\b(\w+ing)\b', word)]


def vowel_count():
    return sum(map(lambda word: len(re.findall(r'[aeiou]', word)), text2.tokens))


def usa_count():
    return sum(map(lambda word: 1 if re.search('U.S.A', word) else 0, text4.tokens))


def not_stopwords(_text):
    words = _text.tokens
    _stopwords = stopwords.words('english')
    diff = set(words) - set(_stopwords)
    return round((len(diff) / len(set(words))) * 100, 3)


def verb_to_verb_ngram(_text):
    _ngrams = nltk.ngrams(_text, 3)
    tagged = list(map(lambda ngram: nltk.pos_tag(ngram), _ngrams))
    matching = [ngram for ngram in tagged if ngram[0][1] == 'VB' and ngram[1][1] == 'TO' and ngram[2][1] == 'VB']
    return matching


if __name__ == '__main__':
    newline()
    different_bigrams()
    newline()
    ngrams()
    newline()
    ngram_graph()
    newline()
    print(words_ending_with_ing())
    newline()
    print(vowel_count())
    newline()
    print(usa_count())
    print(list(map(not_stopwords, texts)))
    newline()
    print("<verb> TO <verb> ngrams, hold on it'll take a while:")
    print(verb_to_verb_ngram(text1))
    print(verb_to_verb_ngram(text2))
    print(verb_to_verb_ngram(text3))
    print(verb_to_verb_ngram(text4))
    print(verb_to_verb_ngram(text6))
