
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

