from nltk.corpus import wordnet
'''
WordNet is basically the library in the NLTK where we can find the synnnyms antonym as well as meaning of the particular word.

'''
# syn = wordnet.synsets("Bad")
# print(syn[0].lemmas()[1].name())

syno = []
anto = []


for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        syno.append(l.name())
    if l.antonyms():
        anto.append(l.antonyms()[0].name())

print(set(syno))
print(set(anto))

