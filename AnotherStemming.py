from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

text = "Text analytics converts unstructured text data into meaningful data for analysis using different linguistic, statistical, and machine learning techniques. While sentiment analysis sounds daunting to brands--especially if they have a large customer base--a tool using NLP will typically scour customer interactions, such as social media comments or reviews, or even brand name mentions to see what’s being said. Analysis of these interactions can help brands determine how well a marketing campaign is doing or monitor trending customer issues before they decide how to respond or enhance service for a better customer experience. Additional ways that NLP helps with text analytics are keyword extraction and finding structure or patterns in unstructured text data. There are vast applications of NLP in the digital world and this list will grow as businesses and industries embrace and see its value. While a human touch is important for more intricate communications issues, NLP will improve our lives by managing and automating smaller tasks first and then complex ones with technology innovation."

tokens = word_tokenize(text)

Stemmed = []

ps_object = PorterStemmer()

for word in tokens:
    Stemmed.append(ps_object.stem(word))

print(Stemmed)