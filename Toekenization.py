from nltk.tokenize import word_tokenize, sent_tokenize

sampleText = "Email filters are one of the most basic and initial applications of NLP online. It started out with spam filters, uncovering certain words or phrases that signal a spam message. But filtering has upgraded, just like early adaptations of NLP. One of the more prevalent, newer applications of NLP is found in Gmail's email classification. The system recognizes if emails belong in one of three categories (primary, social, or promotions) based on their contents. For all Gmail users, this keeps your inbox to a manageable size with important, relevant emails you wish to review and respond to quickly."

words = word_tokenize(sampleText)
'''
If we talk about the words tokenize then it is the proccess in which we have to tokenize the given text into group of words.
'''
sentence = sent_tokenize(sampleText)
'''
In the same sence as of word tokenize sentence tokenize is also used to partition the given sentences into different sentences
'''
print("The given text format has the words which after tokenizing becomes: ")
print(words)
print("\n\n\n")
print("Given text format has sentence which are: ")
print(sentence)