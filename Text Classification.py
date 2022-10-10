import nltk
import random
from nltk.corpus import movie_reviews

all_words = []

for words in movie_reviews.words():
    all_words.append(words.lower())

all_words = nltk.FreqDist(all_words)

print(all_words.most_common(10))
# print(all_words.freq(21822))

print(all_words["stupid"])

# Another Example


