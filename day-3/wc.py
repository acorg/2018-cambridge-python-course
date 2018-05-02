#!/usr/bin/env python

import sys

lines = words = chars = 0

for line in sys.stdin:
    lines += 1
    words += len(line.split())
    chars += len(line)

print(lines, words, chars)
