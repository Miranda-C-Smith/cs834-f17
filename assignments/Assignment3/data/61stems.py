from stemming.porter2 import stem
from collections import defaultdict

def list_duplicates(seq):
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return ((key,locs) for key,locs in tally.items() 
                            if len(locs)>1)
first1000 = []
with open("smallWikiIndex.txt", "r") as inFile:
    for x in range(1000):
        line = inFile.readline().strip("\n")
        first1000.append(line)
    
stemmedWords = []
for index, word in enumerate(first1000):
    stemWord= stem(word)
    print("%s\t%s" %(word, stemWord))
    stemmedWords.append(stem(word))

for dup in sorted(list_duplicates(stemmedWords)):
    print(dup)

