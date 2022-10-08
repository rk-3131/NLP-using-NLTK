'''# Chunking is basically finding the meaning of the given sentence 
Chunk is the grouping of the elements in a way that they are touching or they have some extent of same meaning
Chunking removes the noise from the sentence and it is used to give meaning to the sentence from given set of data
It determines the entity
'''

import nltk

sentence = "I am Radhakrushna Mahadik. I am here to learn the NLTk tools. I will have mastery on them in coming time. Now let's go and learn them"

tokenize = nltk.word_tokenize(sentence)
# print(tokenize)
tags = nltk.pos_tag(tokenize)
# print(tags)
# To create the chunks we have to create the chunk rule it. It can be done by using the chunk rules. and they can be created by using the regular expression used in the python.

myChunkRule = '''myChunk:{<NN?>*<VB?>*}'''

parserObject = nltk.RegexpParser(myChunkRule)
print(parserObject)

parsed_sent = parserObject.parse(tags)
print(parsed_sent)
parsed_sent.draw()

'''
We can even use named entity set instead of chunking hence the named entity can be called automatically
'''

tokenize = nltk.tokenize.word_tokenize(sentence)
tags = nltk.pos_tag(tokenize)
NamedEntity = nltk.ne_chunk(tags)
NamedEntity.draw()