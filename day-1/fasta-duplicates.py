import sys

seen = set()

for inputLine in sys.stdin:
    if inputLine.startswith('>'):
        fastaId = inputLine[1:-1]
        if fastaId in seen:
            print('Hey, I already saw id', fastaId)
            sys.exit()
        seen.add(fastaId)

print(seen)
