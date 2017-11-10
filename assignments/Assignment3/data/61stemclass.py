from stemming.porter2 import stem
from collections import defaultdict

stemclass = defaultdict(list)
with open("1000unstemmed.txt", "r") as infile:
    words = infile.read().splitlines()
    for word in words:
        originalW = word
        stemW = stem(originalW)
        if len(stemW) > 0:
            stemclass[stemW].append(originalW)
classes = dict(stemclass)

with open("stemclass.txt", "w") as outfile:
    for key, value in sorted(classes.items()):
        if len(value) > 1:
            outfile.write(key + " ")
            for word in value:
                outfile.write(word + " ")
            outfile.write("\n")
        


        

    
