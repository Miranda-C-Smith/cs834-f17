#!/usr/bin/env python3
#from nltk.stem import PorterStemmer
#from nltk.tokenize import sent_tokenize, word_tokenize
import urllib3
from bs4 import BeautifulSoup
import PorterStemmer


http = urllib3.PoolManager()

wikiPages = ["https://en.wikipedia.org/wiki/Pocahontas_(1995_film)", "https://en.wikipedia.org/wiki/Virginia_Beach,_Virginia", "https://en.wikipedia.org/wiki/Old_Dominion_University", "https://en.wikipedia.org/wiki/Motorcycle","https://en.wikipedia.org/wiki/Breed-specific_legislation"]

counter = 0
for page in wikiPages:
	response = http.request('GET', page)
	html = response.data.decode('utf8')
	raw = BeautifulSoup(html).get_text()
	filename = "wiki" + str(counter) + ".txt"
	with open(filename, 'w') as outfile:
		print(filename)
		outfile.write(raw.encode('utf8'))
	counter = counter + 1
