#levenshtein distance code from Guy Rutenberg
#https://www.guyrutenberg.com/2008/12/15/damerau-levenshtein-distance-in-python/
def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1,lenstr1+1):
        d[(i,-1)] = i+1
    for j in range(-1,lenstr2+1):
        d[(-1,j)] = j+1
    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i,j)] = min(
                           d[(i-1,j)] + 1, # deletion
                           d[(i,j-1)] + 1, # insertion
                           d[(i-1,j-1)] + cost, # substitution
                          )
            if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition
    return d[lenstr1-1,lenstr2-1]

#will return a list of words from the
#dictionary that start with the same letter
def getDictWordsToCompare(word):
        wordlist =[]
        with open("dictwords.txt", "r") as dictFile:
                for line in dictFile.read().split('\n'):
                        if(len(line) > 0):
                                if(line[0].upper() == word[0].upper()):
                                        #print(line)
                                        wordlist.append(line)
        return wordlist

#take a string and return the first misspelled word
#if nothing misspelt then blank string returned
def findMissspelledWord(string):
        with open("dictwords.txt", "r") as dictFile:
                dictionary = dictFile.read().splitlines()
                upDict = [x.upper() for x in dictionary]
                for word in string.split(' '):
                        if word.upper() in upDict:
                                pass
                        else:
                                return word
        return ""
                                
                
                                
#s="extenssions"
#t="extensions"
#s="brimingham"
#t="birmingham"
#s="doceration"
#t="decoration"
#print(damerau_levenshtein_distance(s,t))
query = input("Enter Query, preferably misspelled: ")

misspelledWord = findMissspelledWord(query)
if(len(misspelledWord) > 0):
        possCorrect =[]
        dictionary = getDictWordsToCompare(misspelledWord)
        for word in dictionary:
                if (damerau_levenshtein_distance(misspelledWord,word) <=2):
                        possCorrect.append(word)
        print("Did you mean:")
        print(possCorrect)
else:
        print("Nothing misspelled")
