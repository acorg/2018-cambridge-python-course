

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
* __cat__   - print file (CATenate)

Unix programs
-------------
Set's up three things:
- Where does the input come from?
- Where does the output go?
- Where do error messages go?

By default all of these are the terminal.

But you can capture the output and redirect it to a file with __>__ e.g.

echo hello there > output.txt


Control characters
------------------
See `man ascii`. Some characters are control characters, they don't print to the output but are interpreted in a special way. For example "carriage return" or "end of text".


GUI
---

Graphical User Interface - designed to be user friendly but also hides alot, like some file extensions and "hidden" files (starting with .)


Command manuals
---------------
* __man__   - Read the MANual for a function e.g. "man ls"

Extra arguments
---------------
Extra arguments for commands can be supplied with "-" e.g. "lm -l"



