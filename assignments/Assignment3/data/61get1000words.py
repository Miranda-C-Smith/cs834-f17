import csv

with open("indexedWords.csv", newline='') as csvfile, open("1000unstemmed.txt", "w") as outfile:
    freader = csv.reader(csvfile, delimiter=',')
    count = 0
    wordList = []
    for row in freader:
        if count > 1000:
            break
        if row[0].isalpha():
            if row[0] not in wordList:
                wordList.append(row[0])
                outfile.write(row[0])
                outfile.write("\n")
                count = count +1
