#!/usr/bin/env python3

from KrovetzStemmer import Stemmer

stemmer = Stemmer()

with open("wiki0.txt", 'r') as infile, open("wiki0Krovetz.txt", "w") as outfile:
        for line in infile.readlines():
                for word in line:
                        outfile.write(stemmer.stem(word))
        
