import sys
import re

pattern = re.compile('^[ACGT]+$')

prefixes = []

for line in sys.stdin:
    if len(line) > 50 and pattern.match(line):
        prefixes.append(line[0:30])

prefixes.sort()

for prefix in prefixes:
    print(prefix)
