import csv
from collections import defaultdict

THRESHOLD = .05
WINDOWSIZE = 75
def diceCoeff(wordA, wordB, index):
    docsWA = index[wordA]
    nDocsWA= len(docsWA)
    docsWB = index[wordB]
    nDocsWB= len(docsWB)
        
    docsWAB = set(docsWA).intersection(docsWB)
    nWinWAB =0
    #In Window
    for doc in docsWAB:
        for Aposition in docsWA[doc]:
            for Bposition in docsWB[doc]:
                if abs(int(Bposition)- int(Aposition)) <= WINDOWSIZE:
                    nWinWAB = nWinWAB + 1
    

    score = (2 * nWinWAB)/(nDocsWA * nDocsWB)
    return score
    

idx = defaultdict(lambda: defaultdict(list))
with open("indexedWords.csv", newline='') as csvfile, open("MLN1stemclass.txt", "r") as stemclass, open("MLN1stemcluster.txt", "w") as clusterFile:
    stemcluster = defaultdict(list)

    #read in the index
    freader = csv.reader(csvfile, delimiter=',')
    for row in freader:
        if row[0][0] == 'a':
            idx[row[0]][row[1]] =(row[2:])
        if row[0][0] == 'b':
            break
    index = dict(idx)
    #read in the stem classes
    for row in stemclass.read().splitlines():
        classStem = row.split()[0]
        classWords = row.split()[1:]
        #compare all pairs of words in a class
        for inx, wordA in enumerate(classWords):
            if inx != len(classWords)-1:
                for wordB in classWords[inx+1:]:
                    #compute dices coefficient
                    score = diceCoeff(wordA, wordB, index)
                    #if the score is above the threshold add WordA and Word B to the cluster
                    #and stop looking at this word A
                    if score >= THRESHOLD:
                        stemcluster[classStem].append(wordA)
                        stemcluster[classStem].append(wordB)
                        break
    #write the new cluster file
    clusters = dict(stemcluster)
    for key, value in sorted(clusters.items()):
        clusterFile.write(key + " ")
        #get rid of duplicates
        words = set(value)
        for word in words:
            clusterFile.write(word + " ")
        clusterFile.write("\n")
                    
                    
                    
                    
                

            
            
