import nltk

'''
As we know chunking is groupin together elements of the given chunkgram
In the same sense Chinking is proccess of removing the groups given in the given Chinkgrams
'''

text = "Apple is fruit. I am Radhakrushna Mahadik. I am here to learn the NLTk tools. I will have mastery on them in coming time. Now let's go and learn them"

tokens = nltk.tokenize.word_tokenize(text)

tags = nltk.pos_tag(tokens)

pattern = '''Chunk:{<NNP>*<PRP?>*<NN?>*<VB?>*}
                    }<MD?>+<CC?>{'''

myObject = nltk.RegexpParser(pattern)

print(myObject)

ans = myObject.parse(tags)
print(ans)
ans.draw()