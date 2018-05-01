
Day 2
=====

More UNIX commands
------------------

__sed__ : Stream EDitor. Program to edit text, acts as a filter, taking from standard input and writing to standard output. Uses regular expressions to match and replace text.

__tr__ : TRanslate sets of characters from one to another.

__awk__ : another program to edit text.

```bash
grep : gabby-metadata.txt | sed 's/^[^:]*:[ \t]*//' | tr , . | awk 'if ((NR % 12) == 0) { printf "\n"; } else { printf "%s,". $0; } }' | sed 's/,$//'
```

_Notes on awk_
You tell it on every line, what to match and what to print. Default is to match everything and print everything (like cat). You can access useful variables like NR for a new line. By default lines are broken up into fields by separating on whitespace.

__cut__ CUTs out parts of lines, based on specified delimiters.

```bash
cat NEO*q | egrep '^[ACGT]+$' | awk 'length > 50' | cut -c1-20 | sort | uniq -c | sort -n -r | head
```

Switch to last directory
```
cd -
```

More  complicated matching of filenames in shell
```bash
ls *[34]-hbv*
ls *[34]-hbv*{readq,fastq}
ls | grep -v fastq
```

Two greater thans append input to the end of a file rather than overwriting it.
```bash
# Create test.txt file
echo "item 1" > ~/Desktop/test.txt

# Append to test.txt file
echo "item 2" >> ~/Desktop/test.txt
```


Back to python
--------------

```python
import sys  # For reading from standard input
import re   # For doing regular expression matching

pattern = re.compile('^[ACGT]+$')  # It's quicker to compile the regular expression beforehand
prefixes = [] # Setup an empty list for the sequences

for line in sys.stdin:
    if len(line) > 50 and pattern.match(line):
        prefixes.append(line[0:30])
        
prefixes.sort()

for prefix in prefixes:
    print(prefix)
```

Executing scripts
-----------------

```
#!/usr/bin/env python
```




