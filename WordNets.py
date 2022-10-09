from nltk.corpus import wordnet


'''
WordNet is basically the library in the NLTK where we can find the synnnyms antonym as well as meaning of the particular word.

'''
syn = wordnet.synsets("Good")
print(syn[10].lemmas()[0].name())
# Above group of statement is given in order to find the synonyms from the set of synonyms. Wordnet has all of them in the order in the form of list

SSet = []
AnSet = []

inputWord = input("Enter the word of your choice: ")

for syn in wordnet.synsets(inputWord):
    for l in syn.lemmas():
        SSet.append(l.name())
    if l.antonyms():
        AnSet.append(l.antonyms()[0].name())

print(set(SSet))
print(set(AnSet))