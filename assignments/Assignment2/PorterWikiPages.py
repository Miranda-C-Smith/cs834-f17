from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from urllib import request
from bs4 import BeautifulSoup


ps = PorterStemmer()

wikiPages = "https://en.wikipedia.org/wiki/Breed-specific_legislation"
response = request.urlopen(wikiPages)
html = response.read().decode('utf8')
raw = BeautifulSoup(html).get_text()
print(raw)
tokens = word_tokenize(raw)
print(tokens)
