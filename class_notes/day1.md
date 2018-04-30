

Day 1
=====


Terry's intro
-------------
It's good to know nothing. We all know very little. Terry knows very little.


Setting up
----------

Homebrew - a package manager. It makes installing command line programs (programs without an application icon) simple. It keeps a repository of all the most used programs so you can download them easily.

Sublime text - a text editor. You can also use others but this has handy features like code highlighting and autocompletion for different languages.


The directory tree
------------------

All the files are stored somewhere in a directory. The desktop is no different, it's just a special folder where all the contents are shown as icons on the desktop.


The shell
---------

Multiple shells, BASH is the most common - "Bourne Again SHell"

You can enter different shells (Control-D to exit a shell)

__Control-L__ to empty the shell screen.

__Control-D__ to end input.


Command list
============

Unix commands
-------------

* __cd__    - Change Directory
* __ls__    - LiSt
* __mkdir__ - MaKe DIRectory
* __touch__ - Just make an empty file or record that it has been updated ("touched" by someone)
* __rm__    - ReMove file
* __rmdir__ - ReMove DIRectory (but only _empty_ directories)
* __echo__  - Print something, useful for producing output in a shell script
* __mv__    - MoVe a file (but can also be used for renaming the file)
* __cat__   - print the contents of a file (CATenate)
* __more__  - shows what's in a file but only a page at a time.
* __less__  - shows what's in a file line by line.
* __pwd__   - Print Working Directory
* __wc__    - Word Count
* __cp__    - CoPy files

(Once in a program like __more__ you can use q to quit - but these are esoteric things for the particular program)

Unix programs
-------------
Set's up three things:
- Where does the input come from?
- Where does the output go?
- Where do error messages go?

By default all of these are the terminal. But you can change them.

Capturing output
----------------

Take the output from the left and supply it as input to a __program__ / __function__ on the left.

```
man cat | less
echo hello there | wc
cat * | wc
```

or, more complex:
```
cat filename.txt | tr ' ' '\n' | tr 'A-Z' 'a-z' | tr -d ',.' | sort | uniq -c | sort -n -r | head -n 20
```
* __tr__    - TransliteRate change characters into other characters
* __sort__  - SORT lines
* __uniq__  - output UNIQue lines

But you can capture the output and redirect it to a __file__ with __>__ e.g.

```
echo hello there > output.txt
```


Control characters
------------------
See `man ascii`. Some characters are control characters, they don't print to the output but are interpreted in a special way. For example "carriage return" or "end of text".

Control-D : End input (kills shell if you are in shell!)
Control-C : Kill the underlying process
Control-L : Empty the shell screen


GUI
---

Graphical User Interface - designed to be user friendly but also hides alot, like some file extensions and "hidden" files (starting with .)


Command manuals
---------------
* __man__   - Read the MANual for a function e.g. "man ls"


Extra arguments
---------------
Extra arguments for commands can be supplied with "-" e.g. "lm -l"





Environment variables
---------------------
Set a variable with the equals sign:

```
x = 4
```

But _access_ a variable using `$` e.g.

```
cat $x
```

Note that this is different for different languages

Special variables
-----------------

`$PATH` A variable name that holds all of the directories that hold programs you might want to run.  When you run a program it looks for a program file in these directories with the same name.

`\bin` - generally system programs
`\usr\bin` - also more systemy things
`\usr\local` - user installed programs

You can use `which` to find where a program is being called from e.g. `which python`.

But note things like `type cd` - a shell built in.


String matching
---------------

Use `*` to match any characters, e.g. for selecting multiple files.

Cat all files on desktop ending in .txt:

```
cat ~/Desktop/*.txt
```

Quotes in shell
---------------

Inside the shell variables in _double_ quotes are expanded but variables in _single_ quotes are not. e.g.:

```
x=4
echo "$x"
echo '$x'
```


Loops in shell
--------------


Shell as a programming language
-------------------------------

Can still do programming in the shell, for example

For loops
```
for i in *
do
echo $i
done
```

If statement
```
if [ $x = 4 ] # Note spaces
then
echo yes
fi
```

Big difference is that variables are called with the `$` symbol and otherwise things are looked up in your path.


Python intro
============

Python is unusual because indentation matters!

For example in `if` loops
```python
x = 4

if x == 5:
	print('really big')
else:
	print('not so big')
```

Or in `for` loops
```python
for wanted in ['butter', 'cheese', 'celery']:
  	print('now we have to find', wanted)
```


Objects in python
-----------------

Functions are attached to objects in python and pretty much everything is an object. Even strings are objects! They are not just a bunch of characters, they also contain a reference to an underlying 'prototype' string object, when you create a string it inherits a lot of functions from the base generic string object.  e.g.

```python
mystring = "hello world"
print(mystring.startswith('h'))

# Or call it directly on the string:
print("hello world".startswith('h'))
```

You can use `dir()` to list all the functions attached to an object. e.g.
```python
mystring = "hello world"
dir(mystring)

# Or call it directly on the string:

dir("hello world")
```


Dictionaries
------------

Dictionaries can contain anything as values (and as keys!).  Very useful and flexible. They are different from lists because there are not only values but also keys. They aren't ordered.

```python
# Make a new empty dictionary:
d = {}

# Add a list
d['age'] = (3, 5, 21)

# Recall from a list
d['age']

a, b, c = 1, "hi", 45
```

Dictionaries can be sorted, but it only sorts the keys, not the values.


Set
---

A set for storing values:

```python
seen = set()
```

Sets are not ordered and contain unique values


List
----

Lists are ordered and can contain anything, they can be made:

```python
newlist = [1, 2, 3]
```

__CAREFUL__
Strings used in the context of a list will be treated like a list! i.e.:
```python
for x in "abcfjse":
	print(x)
	
print(sorted("abcfjse"))
```


Converting between dictionaries and lists
-----------------------------------------

Sometimes you want to convert a dictionary to a list, so that you can do things like sort the items (which can't be done with a dictionary). It can be done by iterating through the dictionary tuples and appending them to a list:

```python
# Assume wordCounts is a dictionary
newlist = []
for (word, count) in wordCounts.items():
  newlist.append((count, word))
```


Difference between functions that return and object and functions that modify an object
---------------------------------------------------------------------------------------

Some functions change the object themselves when called e.g.:

```python
newlist = [2,3,1,0]
newlist.sort()
print(sort)
```

Some functions do something but return another object leaving the original object untouched e.g.:

```python
newlist = [2,3,1,0]
sortedlist = sorted(newlist)
print(newlist)
print(sortedlist)
```




