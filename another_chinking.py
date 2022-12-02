import nltk

text = "I am Radhakrushna Mahadik. I am here to learn the NLTk tools. I will have mastery on them in coming time. Now let's go and learn them"

tokens = nltk.tokenize.word_tokenize(text)

for word in tokens:
    if word in nltk.corpus.stopwords.words("english"):
        tokens.remove(word)

after_tagged = nltk.tag.pos_tag(tokens)


myChunk = '''Rule:{<NN?>*<VB?>*}
                    }<MD>*<CC>{'''

parserObject = nltk.RegexpParser(myChunk)

sentence = parserObject.parse(after_tagged)
sentence.draw()

