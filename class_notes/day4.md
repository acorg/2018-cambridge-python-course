#Mailing list

Started a google group: camhackers@googlegroups.com

#Classes

Classes are akin to factories. We talked through classes using a bag factory analogy.
The bag factory (i.e. class) provides the capacity to make bags (i.e. objects) but not their actual production.
A method is a function within a class.

`def __init__(self)` - initialise a function (get the bag set up for a customer)

*The cool kids use "self" but you can use any variable name.*

Special class methods allow the use of built-in functions in classes.
e.g. `def __len__(self)` enables the use of the `len` function to determine the length of an object. 
Other special classes include `__str__` for printing strings and `__gt__(a,b)` for determining whether a>b.

Subclasses allow the different implementation of methods which are already defined by a class.
Using the bag factory example, if we wanted to open a new subsidiary of our bag-making company in the UK which measures the bags in inches rather than cm, we wouldn't need to redesign the whole factory, we could just adjust our measurement function. The bags are identical from the two factories, only how the measurements are reported differ. The subclass inherits the attributes of the parent class.

If you use strings to describes classes and functions, you can then use the option help() to see documentation for these classes and functions.

#Places to look for help

python.org
stackoverflow - look at the date (old - is it out of date or has it stood the test of time?), reputation of person, upvoting
pydoc - find out about python classes e.g. to find out about the function `len` enter `pydoc len` on the command line.
python help() function
python dir(*object*) function 

#Jupyter

Jupyter is an integrated development environment for python.

It can be installed using pip:

`pip3 install jupyter`

and run from the command line:

`jupyter notebook`

Go to new -> python3

`Ctrl-return` - run and stay in the same cell
`Shift-return` - run and create a new cell

Three different types of cell:
code, markdown, and raw notebook stuff (Terry doesn't even know what the third one is).

Jupyter creates an .ipynb file rather than a .py file - it contains data from the notebook as well as the code.

# Job control

`Ctrl-Z` - put job in the background
`Ctrl-C` - shut down job
`fg` - continue job in the foreground
`bg` - continue job in the background
`bg %x` - resume job x in the background
`Ctrl-D` - kill job
`jobs -l' - list jobs
`kill %x` - kill job x
`&` - at the end of command, run but don't wait for process to finish

# Misc

Stephen Wolfram blog - read post of computational essays.
Javascript wat 
