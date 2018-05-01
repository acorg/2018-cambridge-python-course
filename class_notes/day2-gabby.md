# Day2 G Notes

1 May

## Gabby's notes

Pelican notebooks: uses python to create websites. Terry keeps his notes on Pelican.

Github pages would be the equivalent, does not require to set up your own server.

Python modules- [“standard library”](https://docs.python.org/3/library/) wiki, very extensive.

Biopython [tutorial cookbook](http://biopython.org/DIST/docs/tutorial/Tutorial.html)

Barbara and Terry wrote [d](https://github.com/terrycojones/dark-matter)[arkmatter](https://github.com/terrycojones/dark-matter). A set of python tools to study next gen seq

## Metadata problem2

[Link](https://github.com/gmkov/python-course-camb-2018/blob/master/gabbys-problems/pr2-metadata.md) to git repo by @gmkov with problem 2

Example raw data

```
RECORD ID: site1test
----  
Record from FILE: GLAMA_20170628_041819
Time and Date of Calc.:   04:21:32 2017-06-28
Total No. of Pixels:      2460574 px
Tot. No. of Light Pixels: 149352 px
Gap Fraction:             6,07%
Part of Hemisph. Taken:   92,00%
Cut Level btw L-D pixels: 200
----  
Canopy Openness:          6,29%
Canopy Closure:           93,71%
Canopy Cover Index:       68,99%
Modified CaCo Index:      79,87%
----  

RECORD ID: kitchen 
----  
Record from FILE: GLAMA_20170714_194041
Time and Date of Calc.:   19:41:56 2017-07-14
Total No. of Pixels:      2460574 px
Tot. No. of Light Pixels: 112572 px
Gap Fraction:             4.58%
Part of Hemisph. Taken:   91.94%
Cut Level btw L-D pixels: 105
----  
Canopy Openness:          4.57%
Canopy Closure:           95.43%
Canopy Cover Index:       63.58%
Modified CaCo Index:      70.61%
----  
```



1. All the lines we want have a colon :  in them. So first task is to get rid of all the other lines

```
#grep goes by line, and grabs those with :
grep : gabby-metadata.txt

# sed is a filter, read from stdin and makes standard ouput
# edits texts. write regular expressoin
# start of the line, any character that is not a colon
# \t is a tab
grep : gabby-metadata.txt | sed 's/^[^:]*:[\t]*//' |head

# now we have a list of things, but there are some commas,
# if we are making a .csv file the commas will confuse things
# translate , into .

grep : gabby-metadata.txt | sed 's/^[^:]*:[\t]*//' | tr , . | head

# use awk
# mod is the remainder of a division, the line number mod 12=0, 
# then we are at the start of a new record
# then remove comma at the end of the line

grep : gabby-metadata.txt | sed 's/^[^:]*:[\t]*//' | tr , . | awk 'if (NR % 12)
 = 0 {printf "\n" } else { printf "%s,", $0; } }' | sed 's/,$//'

```



## AWK examples

Regular expressions language to match things.

```
# example of awk work
# prints the second field of each line
awk '{print $2}' < gabby-metadata.txt

# this doesnt print, just shows lines with less than 5 records
awk '{NR < 5}' < gabby-metadata.txt

# print last thing on each field
awk '{print $NF}'
```



## Cut examples

```
# prints out second field, you give it the delimitor
# cut, give me second field, separators
cut -f2 -d ' '
```



## Example fastq files checking

Get out lines of DNA from fastq files

```
# extract lines of DNA, that start with ACGT
# extended grep, matches on regular expressions (grep just does strings)
# egrep is more generic than grep, it can search for 
# "an S at the start of a word, a vowel in the middle", 
# grep can only look for patterns in 
# ^ start of the line, + one or more of these characters (* would be 0 or more),
# $ go to end of line (so that it doesnt match to a sequence name with a ACGT)

cat NEO*q| egrep '^[ACGT]+$' | head

# extract first 20 characters
cat NEO*q| egrep '^[ACGT]+$' | awk 'length > 50 '| cut -c1-20 | head

# to check the first 20 characters and see if they are repeated
# then sort it in reverse, to check whether there are sequences 
# repeated at the starts many times

cat NEO*q| egrep '^[ACGT]+$' | awk 'length > 50 '| cut -c1-20 | sort | uniq -c |
 sort -n -r | head

```



## Same example but in Python

We are trying to replicate the command line solution above in Python


```
# write script shell-equivalent-fastq.py 
# cat NEO*q| egrep '^[ACGT]+$' | awk 'length > 50 '| cut -c1-20 | sort | uniq -c | sort -n -r 

import sys #import for system preferences
import re #import for regular expression

# make regular expression and compile it before the program
# so that then it can just be called
# regular expression language similar across languages

patternacgt = re.compile('^[ACGT]+$')

#collect preffixes in an array
prefixes = []

for line in sys.stdin:
    if len(line) > 50 and patternacgt.match(line):
        prefixes.append(line[0:30])

prefixes.sort()

for prefix in prefixes:
    print(prefixes)

```



```
# to execute our python script
myfastq-file.fastq | python3 shell-equivalent-fastq.py 
```



## Looking for files in the shell

Shell version of regular expressions to look for
in shell * means any character 
in python you use . to match any character or value
*| are shell medicharacters

```
# match any string of characters, [any] 3 or 4,
ls *[43]-hbv*
```

Matching with egrep. Testing on the shell their behaviour

```
# it'll return when it matches
egrep '.a'
egrep '.a$'
egrep '.*a$'
egrep 'a[gc]*a'
egrep 'a(gc)*a'

# OR
ls NEO*-hbv-*{fastq,read-counts}

# to exclude files, not easy with regular expressions
# parse it to grep
# grep -v throws away the matches
ls NEO* | grep -v 

```



## How to call the shell from my Python


[Check](https://docs.python.org/3.5/library/subprocess.html) subprocess.checkoutput documentation

You need to capture the output


> `stdout`

> Captured stdout from the child process. A bytes sequence, or a string if [``run()``](https://docs.python.org/3.5/library/subprocess.html#subprocess.run) was called with ``universal_newlines=True``. ``None`` if stdout was not captured.
If you ran the process with ``stderr=subprocess.STDOUT``, stdout and stderr will be combined in this attribute, and [``stderr``](https://docs.python.org/3.5/library/subprocess.html#subprocess.CompletedProcess.stderr) will be ``None``.



We are running the date command, but we are not capturing, so 



## Arithmetic in shell

```
# must put $(())
echo $(( 3 + 4 ))
```



## Shell script example

Write it on text editor

```
#!bin/bash
a=4
echo "Hello is $a"
```

Wont work, make it executable

```
# Make shell script executable (check permissions)
ls -la
chmod +x shell-script.sh 
```

## Changing your $PATH

```
# have a look
echo $PATH
```

A . in your path makes path look in your current directory
2 ways to modify your path:

**1) Temporarily**

```
# add . to the start of $PATH
PATH=".:$PATH"


```


**2) Permanently**

```
# manually add the .
vim ~/.bash_profile

ZZ # to exit
echo $PATH
```

## Writing python scripts

```
#you can call python directly from where installed

#!/usr/bin/python3

# call environment (have env installed)
# Env will look in your environment, and figure out where python is and run it.

#!/usr/bin/env python3


```



# Sliding Window challenge



### Fastq file format

**Identifier**
@ + identifier + sequence + +sign + identifier

**Quality string**
Every fourth line is a quality string (how likely is to be correct). Quality strings lines can be any printable characters, problem is that quality data sometimes can start with an @

The quality and the sequences can be spread over multiple lines nearly randomly
In fasta file types, next sequence starts with a > sign (much simpler)

All of the above make parsing fastq files very difficult. **Biopython makes it very easy**


### Biopython

```
#install
pip3 install BioPython

```

Check BioPython documentation [here](http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc49)

 python script

```
#!/usr/bin/env python3
from Bio import SeqIO
for seq_record in SeqIO.parse("test.fastq", "fastq"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record)
```

```
#make .py executable
chmod +x windowed.sequences.py

```

SeqRecord object in biopython have attributes. [section 5.1](http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc49)
seqrecord class has __function__ , print looks for function

We know that this record is not a string, is a SeqRecord object

```
# now turn object into a string, with str
# to get the sequence
# reads fastq and reads the sequences

for record in SeqIO.parse('test.fastq', 'fastq'):
    sequence=str(record.seq)
    print(sequence)
    
```


Now to do analysis we are going to make a function (analyze)

```
# define function, for now is not doing anything
# seq is a new variable
def analyze(seq):
    pass
#call the function
for record in SeqIO.parse('test.fastq', 'fastq'):
    sequence=str(record.seq)
    analyze(sequence) 
    
       
# TEST
 
#!/usr/bin/env python3

from Bio import SeqIO

def analyze(seq):
    print('I was called with' s)

for record in SeqIO.parse('test.fastq', 'fastq'):
    sequence=str(record.seq)
    analyze(sequence)
   

```



define functions

```
def analyze(seq):
    print('The sequence is', seq, 'and has length', len(seq))
    start = 0
    stop = start + windowSize 
    len = len(seq)

    def countGs(s):
        return s.count('G')

    while stop < length: #we are going to ignore the last bit of the sequence that does not have enough reads to fill a window
        window = seq[start:stop] #cutting the piece with []
        print('   The next window is' window)
        start += windowSize
        stop += windowSize
        
        
```

### error checking in python

```

#set options within program
#sys.argv is a list of arguments, if it's only 1 then there are no arguments
# sys.argv[1] is the second thing on list
./windowed-sequences.py analyze1
./windowed-sequences.py analyze2

# %s getting the value of a variable into a string
# % sys.argv[0] is the name of the program
# then when %s is on at the start of the string, 
# it will put the name of the program
# %i would be for an interger, %d a decimal

# option 1 (more complicated but handy when many integrations)
errorMsg = ('%s: Unkown option...' % sys.argv[0]) 
# equivalent, in python you can add strings
errorMsg = (sys.argv[0] + 'Unkown option...')



 
```


All files have** stdin, stdout, std error.** We should write errors to stderror not stdoutput, otherwise the error will be stored in the output

```
# this should fail
windowed.sequences.py analyze2kkkk

#in order for an error message to pop up
# must specify to print the error in stderr
else:
    errorMsg = ('%s: Unkown option...' % sys.argv[0]) # this would add to the error message
    print(errorMsg, file=sys.stderr) # file= so that it does not save the error in the output
    sys.exit() # if we dont have a function then exit...
    
 
# 1> > is stdout
# 2> is stderr  
 windowed.sequences.py >output 2>error 
 
 
# you can give the exit a value, an exit status
# in the shell, a non zero exit code means the previous command did not work

gabrielamontejokovacevich$ sflsdl
-bash: sflsdl: command not found
gabrielamontejokovacevich$ echo $?
127


 
```

### error checking in BASH scripts

test

```

# putting -e at the start will check all the errors
#!/bin/bash -e


which test

bash
type test # it's a builtin

# THESE [ ] are actually a program
cd /bin/
la -la # you will see a prgram called [

# they are testing, need space
if [ -s error ] #-s true if file exists, from test function
then
    echo 'The error file is not empty!' >&2 #save standard error in shell
    exit 1
fi


```


**Script version 1 for making windows**

Not flexible, user cannot define options without editing source code

```
#!/usr/bin/env python3
import sys #access to the command line
from Bio import SeqIO

windowSize = 10

def analyze1(seq):
    print('The sequence is', seq, 'and has length', len(seq))
    start = 0
    stop = start + windowSize 
    len = len(seq)

    def countGs(s):
        return s.count('G') #define another function within function that will be used by analyze

    while stop < length: #we are going to ignore the last bit of the sequence that does not have enough reads to fill a window
        window = seq[start:stop] #cutting the piece with []
        print('   The next window is' window)
        print('   The G count is' countGs(window))
        start += windowSize
        stop += windowSize

def analyze2(seq):
    print('fake analysis!') 

# let user select analysis type they want to do

if sys.argv[1] == 'analyze1': #users first argument to program is analyze1 [1], then do...
    analyze1(sequence)
elif sys.argv[1] == 'analyze2': ##users irst argument to program is analyze2 [1], then do...
    analyze2(sequence)
else:
    errorMsg = ('%s: Unkown option...' % sys.argv[0]) # this would add to the error message
    print(errorMsg, file=sys.stderr) # file= so that it does not save the error in the output
    sys.exit() # if we dont have a function determined by user that exists, then exit...


# analysis
for record in SeqIO.parse('test.fastq', 'fastq'):
    sequence=str(record.seq)
```



## Improve python script - more flexibility

We want to be able to set options from the command line for our program.

```
import argsparse
# to create an argsparse object
# to determine options of an argument you create

```

filter-fasta.py as an example (from darkmatter)

We are going to parse window size into a function

Commenting in python

* # ignored by python
* comments in strings can be used for help()
* “”” embed new lines onto strings


help(function)
help is actually looking for function.__doc__ and prints comments in string 


The argument parser looks for unique preffixes for options you dont need to write the whole thing.

Final script sightly annotated. Might contain typos

```
#!/usr/bin/env python3
import sys #access to the command line
from Bio import SeqIO

########
# define functions the prgram will use
def analyze1(seq, windowSize):
    print('The sequence is', seq, 'the window size is', windowSize,
        'and has length', len(seq))
    start = 0
    stop = start + windowSize 
    len = len(seq)

    def countGs(s):
        return s.count('G') #define another function within function that will be used by analyze

    while stop < length: #we are going to ignore the last bit of the sequence that does not have enough reads to fill a window
        window = seq[start:stop] #cutting the piece with []
        print('   The next window is' window)
        print('   The G count is' countGs(window))
        start += windowSize
        stop += windowSize

def analyze2(seq, windowSize):
    print('fake analysis!') 

# add function that does windows, with a step
def analyze3(seq, windowSize):
    print('The sequence is', seq, 'the window size is', windowSize,
        'and has length', len(seq))
    start = 0
    stop = start + windowSize 
    len = len(seq)

    def countGs(s):
        return s.count('G') #define another function within function that will be used by analyze

    while stop < length: #we are going to ignore the last bit of the sequence that does not have enough reads to fill a window
        window = seq[start:stop] #cutting the piece with []
        print('   The next window is' window)
        print('   The G count is' countGs(window))
        start += windowSize
        stop += windowSize


########
# define arguments
parser = argparse.ArgumentParser(
    description='Script to do a window analysis')

parser.add_argument(
    '--analyzeFunction', default='analyze1', # must add a default to arguments
    choices=('analyze1', 'analyze2'),
    help='The analysis type')

parser.add_argument(
    '--windowSize', 'w', type=int, default =10, # must add a default to arguments
    help='The sliding window size')

parser.add_argument(
    '--verbose', 'v', action='store_true', default=True, # must add a default to arguments
    help='TIf given print extra helpful output')

args = parser.parse_args()

########
# what to do in case any of the options are specified (other than default)
if args.verbose:
    print("hey welcome to version 0.0.0.01 of our"
        "program....")

if args.analyzeFunction == 'analyze1':
    analyzeFunc = analyze1
else:
    analyzeFunc = analyze2

########
# analysis
for record in SeqIO.parse('test.fastq', 'fastq'):
    sequence=str(record.seq)
    analyzeFunc(sequence, args.windowSize)
    
    
```



# Git and GitHub

Git: a version control system

function git blame (it can tell you who made the change that bugged the code)

### github

Example https://github.com/acorg/slurm-pipeline

Copy/Clone, copy url and in terminal

```

# you need to tell git
git clone git@github.com:acorg/slurm-pipeline.git

# this https always works
git clone https://github.com/acorg/slurm-pipeline.git

 type git
> git is hashed (/usr/local/bin/git)
 git --version
git version 2.17.0


```


To find files that havent been committed to github

```
git status
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)

    .DS_Store
    scripts/
    shell-script.sh
    slurm-pipeline/
    useful.code.gabby.md

nothing added to commit but untracked files present (use "git add" to track)

# to check changes in modified files
git diff .

# lines that have disappeared will appear with a - (in read)
# get back the version of file from last commit
# changes the file in place
git checkout -- README.md


# to see log of commits
git log -v -v -v 



```


How to start a git repository 

```
# make directory with work
git init
# to start tracking a file (staging, its staged to be committed)
git add file.txt
git commit -m "comment about the commiting"
git status

git remote add origin https....
push -u origin master

# if you create something on github
# or want to pull collaborators updates on code
git pull origin master

# before you can push your changes it will tell you to pull
# if there are differences in the file
# then when you pull it might be able to do merging
# or it might tell you to solve the conflict manually, then pull

```

**Short intro to forking, editing, pull requests**

First fork someone elses code, make changes on it, comment on why how you did them, then do a Pull request to the code owner to see if they want to merge your changes to their master code








