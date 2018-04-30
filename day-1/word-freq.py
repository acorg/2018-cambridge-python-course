import sys
from collections import defaultdict

# wordCounts = {}
wordCounts = defaultdict(int)
punc = "',."

for inputLine in sys.stdin:
    inputLine = inputLine[:-1]
    for word in inputLine.split():
        for x in punc:
            word = word.replace(x, '')
        # word = word.replace("'", "").replace(",", "").replace(".", "")
        wordCounts[word] += 1
        # if word in wordCounts:
        #     wordCounts[word] += 1
        # else:
        #     wordCounts[word] = 1

# print(wordCounts)

# newlist = [(count, word) for (word, count) in wordCounts.items()]

newlist = []
for (word, count) in wordCounts.items():
    newlist.append((count, word))

# newlist.sort(reverse=True)

for count, word in sorted(newlist, reverse=True):
    print(word, count)


def keyfunc(t):
    return t[1]

# newlist.sort(reverse=True, key=keyfunc)

for word in sorted(wordCounts, reverse=True, key=keyfunc):
    print(word, wordCounts[word])
