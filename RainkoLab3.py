import nltk
from nltk import text
from nltk.book import *
from nltk.corpus import stopwords
from nltk.corpus import movie_reviews, brown
from collections import Counter
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import wordnet as wn
from nltk.util import pr


def exc_header(number):
    print('Zadanie nr'.format(number))


def zadanie5():
    exc_header(5)
    words = brown.words(categories='adventure')
    print(words.count('mountains'))
    print(words.count('ocean'))
    print(words.count('Bungee jump'))


def top10MostOftenOccurringWords():
    counted_words = Counter(inaugural.words()).most_common(10)
    print(counted_words)


def sentiments():
    words_to_check = ['journalist.n.01', 'writer.n.01', 'actor.n.01', 'singer.n.01']
    for word in words_to_check:
        breakdown = swn.senti_synset(word)
        print(word)
        print(breakdown)


def meaning_meter(word1, word2):
    word1Synset = wn.synset(word1 + ".n.01")
    word2Synset = wn.synset(word2 + ".n.01")
    print(word1Synset.path_similarity(word2Synset))

def gutenberg_metrics():
    texts = gutenberg.fileids()
    for text in texts:
        print(text)

        text_words = gutenberg.words(text)
        word_lengths = list(map(lambda word: len(word), text_words))
        avg_words = sum(word_lengths) / len(text_words)
        print("Avg character word count for " + text + ": " + str(avg_words))

        text_sents = gutenberg.sents(text)
        sents_lengths = list(map(lambda sent: len(sent), gutenberg.sents(text)))
        avg_sents = sum(sents_lengths) / len(text_sents)
        print("Avg word count in sentence for " + text + ": " + str(avg_sents))

def frequencies():
    brown.cr09


if __name__ == "__main__":
    print('Zadanie nr 1')
    print(gutenberg.fileids())
    print('Zadanie nr 2')
    print(inaugural.fileids())
    print('Zadanie nr 3')
    print(movie_reviews.categories())
    print('Zadanie nr 4')
    print(inaugural.sents('1909-Taft.txt'))
    print('Zadanie nr 5')
    zadanie5()
    print('Zadanie nr 6')
    top10MostOftenOccurringWords()
    print('Zadanie nr 8')
    sentiments()
    print('Zadanie nr 9')
    word_pairs = [
        ['boy', 'lad'], ['journey', 'voyage'], ['coast', 'hill'],
        ['monk', 'slave'], ['food', 'fruit'], ['journey', 'car']
    ]
    similarities = list(map(lambda pair: meaning_meter(pair[0], pair[1]), word_pairs))
    print('Zadanie nr 10')
    gutenberg_metrics()
#     Więc kolejność w liście się zgadza
