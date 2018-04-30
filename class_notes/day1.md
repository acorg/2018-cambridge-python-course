Day 1
=====

Terry's intro
-------------

It's good to know nothing. We all know very little. Terry knows very
little.


Setting up
----------

Homebrew - a package manager. It makes installing command line programs
(programs without an application icon) simple. It keeps a repository of all
the most used programs so you can download them easily.

Sublime text - a text editor. You can also use others but this has handy
features like code highlighting and autocompletion for different languages.

The directory tree
------------------

All the files are stored somewhere in a directory. The desktop is no
different, it's just a special folder where all the contents are shown as
icons on the desktop.

The shell
---------

Multiple shells, BASH is the most common - "Bourne Again SHell"

You can enter different shells (Control-D to exit a shell)

__Control-L__ to empty the shell screen.

__Control-D__ to end input.


Unix command line
=================

Unix commands
-------------

* __cd__    - Change Directory
* __ls__    - LiSt
* __mkdir__ - MaKe DIRectory
* __touch__ - Make a new empty file or set the modification date on an existing file to now (i.e., make it look like the file was just "touched" by someone)
* __rm__    - ReMove file
* __rmdir__ - ReMove DIRectory (but only works on _empty_ directories)
* __echo__  - Print something, useful for producing output to feed into in a program
* __mv__    - MoVe a file (to another directory or to have another name, or both at once)
* __cat__   - print the contents of a file (CATenate)
* __more__ - shows what's in a file, but only a page at a time (use SPACE
  to advance a page, `q` to quit).
* __less__ - shows what's in a file, but only a page at a time (use SPACE
  to advance a page, `q` to quit). Just like `more` but more powerful and
  modern.
* __pwd__   - Print Working Directory
* __wc__    - Word Count - shows counts of lines, words, characters.
* __cp__    - CoPy a file

(In programs like __more__ and __less__ you can use `q` to quit and `/` to
search - but these are esoteric things for the particular program. See
their `man` pages.)

Unix programs
-------------

Always have three things:

- Where does their input come from?
- Where does their output go?
- Where do their error messages go?

By default all of these are the terminal. But you can change them.

Capturing output
----------------

Take the output from the left and supply it as input to a __program__ /
__function__ on the right.

```
man cat | less
echo hello there | wc
cat * | wc
```

or, more complex:

```
cat filename.txt | tr ' ' '\n' | tr 'A-Z' 'a-z' | tr -d ',.' | sort | uniq -c | sort -n -r | head -n 20
```

* __tr__ - TransliteRate characters into other characters (e.g., `tr A-Z
  a-z` to change to lower case)
* __sort__  - SORT lines
* __uniq__ - output UNIQue lines (its input must already be sorted). Add
  `-c` to also output a count of the number of times lines are repeated.

You can capture the output and redirect it to a __file__ with __>__ e.g.

```
echo hello there > output.txt
```

Control characters
------------------

See `man ascii`. Some characters are control characters, they don't print
to the output but are interpreted in a special way. For example "carriage
return" or "end of text".

Control-D : End input (kills shell if you are in shell!)
Control-C : Kill the underlying process
Control-L : Empty the shell screen

GUI
---

Graphical User Interface - designed to be user friendly but also hides a
lot, e.g., some file extensions and "hidden" files (those that start with
`.`).

Command manuals
---------------
* __man__   - Read the MANual for a function e.g., `man ls`.


Extra arguments
---------------
Extra arguments for commands can be supplied with "-" e.g., `ls -l`.


Environment variables
---------------------
Set a variable with the equals sign:

```
x=4
```

Note that in the shell you cannot have spaces before or afer the `=`.

But _access_ a variable's value using `$` e.g.

```
echo $x
```

Note that this is different for different languages. In Python you don't
need the initial `$` to get a variable's value.

Special variables
-----------------

`PATH` A variable that holds all of the directories that hold programs you
might want to run.  When you type a program name, the shell (usually
`bash`) looks for a file with that name in the `PATH` directories in order
to execute it.

`/bin` - generally (ancient) system programs
`/usr/bin` - also more system-y things
`/usr/local` - user installed programs (this is where brew keeps things)

You can use `which` to find where a program is found in your `PATH` e.g.`
`which python`.  Also the `type` command does the same thing.

But note things like `type cd`. `cd` is a shell built-in function.


String matching
---------------

Use `*` to match any characters, e.g., for selecting multiple files.

Cat all files on your desktop ending in `.txt`:

```
cat ~/Desktop/*.txt
```

Quotes in shell
---------------

Inside the shell variables in _double_ quotes are expanded but variables in
_single_ quotes are not. e.g.,:

```sh
$ x=4
$ echo "$x"
4
$ echo '$x'
$x
```

Shell as a programming language
--------------

Can still do programming in the shell, for example

For loops

```sh
$ for i in *
> do
>     echo $i
> done
```

If statement

```sh
$ if [ $x = 4 ] # Note spaces
> then
>     echo yes
> fi
```

Variable values are obtained with the `$` symbol and otherwise things
(commands) are looked up in your path.


Python intro
============

Python is unusual because indentation matters!

For example in an `if` statement:

```python
x = 4

if x == 5:
	print('really big')
else:
	print('not so big')
```

Or in `for` loops:

```python
for wanted in ['butter', 'cheese', 'celery']:
  	print('now we have to find', wanted)
```


Objects in python
-----------------

Functions are attached to objects in python and pretty much everything is
an object. Even strings are objects! They are not just a bunch of
characters, they also contain a reference to an underlying 'prototype'
string object, when you create a string it inherits a lot of functions from
the base generic string object.  e.g.,

```python
mystring = "hello world"
print(mystring.startswith('h'))

# Or call startswith directly on the string:
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

Dictionaries can contain anything as values (and as keys!).  Very useful
and flexible. They are different from lists because:

* there are not only values but also keys
* they are not ordered
* keys must be unique (unlike in a list where things can be repeated)
* (implementation detail) keys can be looked up in (expected) constant
  time. In a list you have to walk through the list comparing elements.

```python
# Make a new empty dictionary:
d = {}

# Add a key whose value is a tuple of 3 integers.
d['age'] = (3, 5, 21)

# Recall the value of a key.
d['age']
```

Calling `sorted(d)` where `d` is a dictionary will get you a sorted list of
the dictionary's keys.  It's a bit harder to sort by the dictionary's
values.

Unpacking assignment
------------------------

```python
a, b, c = 1, "hi", 45
```

Set
---

A set for storing values:

```python
seen = set()
```

Sets are not ordered, contain unique values, can be accessed quickly
(unlike a list). A set is equivalent to a dictionary that has no values.


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

Sometimes you want to convert a dictionary to a list, so that you can do
things like sort on the values (which can't be done quite so easily with a
dictionary). This can be done by iterating through the dictionary tuples
and appending them to a list:

```python
# Assume wordCounts is a dictionary
newlist = []
for (word, count) in wordCounts.items():
  newlist.append((count, word))
```

This is a bit inefficient because all the data in the dictionary is
copied. See the code for day 1 to see alternatives.


Difference between functions that return and object and functions that modify an object
---------------------------------------------------------------------------------------

Some functions change the object themselves when called e.g.,:

```python
newlist = [2,3,1,0]
newlist.sort()
print(newlist)
```

Some functions do something but return another object leaving the original
object untouched e.g.,:

```python
newlist = [2,3,1,0]
sortedlist = sorted(newlist)
print(newlist)
print(sortedlist)
```
