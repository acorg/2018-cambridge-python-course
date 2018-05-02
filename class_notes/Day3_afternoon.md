# Class notes - Day 3, Afternoon

## Speed on the Command Line
Some command line shortcuts:
* `up-arrow`: scroll back through previous commands
* `alt-B`: go back a whole word along line
* `alt-f`: go forward by a word
* `alt-d`: delete word after cursor
* `alt-backspace` : delete word before cursor
* `ctrl-k`: delete from cursor to end of line
* `ctrl-a`: go to start of line
* `ctrl-e`: go to end of line
* `ctrl-y`: pulls back the text that you have deleted
* `ctrl-f`: forward by character
* `alt-t`: swaps words around (moves cursor along by a word)
* `ctrl-t`: swaps characters around (moves cursor along by a character)
* `alt-.`: returns previous argument from previous command
* `ctrl-r`: reverse incremental search (searches through bash history and finds last command with same starting character). 
Press `ctrl-r` repeatedly to toggle through possibilities
*`ctrl-l`: clear screen

In general, `ctrl` does things on characters, `alt` does things on words.

`less ~/.bash_history`: search through previous bash commands
`set | less`: show all environment variables

Within `less` program:
`/` : search
`n`: previous hit
`N`: next hit
`q`: exit less
`g`: go to bottom of file
`G`: go to top of file
`return`: scroll down 1 line

## vim
`vim`: text editor that can be run on command line. Useful for editing remote files

## Amazon web services
Allows any individual to rent a web server
Good for programs which require lots of processing power and/or memory

## Using ssh to reach the cluster
### Accessing remote servers
Cluster: collection of servers
`ssh`: secure shell
You can use `ssh` to run a shell command on another machine
`ssh + machine_name + command`: run a command in shell on another machine
`ssh + machine_name`: open up shell on another machine
`logout`: logout of remote server

### Setting permissions on remote server
Make directory called `.ssh` - must have permissions 700
`chmod og= .ssh`: remove all permissions for other people and my group in .ssh directory

Make file called `authorized_keys`: put ssh public key (see below) in here - set permissions to be 600
`chmod og= authorized_keys`: remove all permissions for other people and my group in authorized_keys directory

### Generating ssh key:
* `ssh-keygen -t rsa`: generates private and public ssh key
* choose file in which to save key
* choose if want to password protect key
* Add public key to authorised key files folder

## Screen: or how to have multiple sessions in parallel on a server which does not terminate when you close computer or lose connection
`screen`: 
*allows you to set up multiple terminals. 
*allows program in screen to keep running even if connection drops or switch off computer (keeps processes running in background)

`screen -ls`: lists active screen sessions
`screen -x`: reconnect to previous screen session
`screen -s` + session_name: give name to a specific screen session

### Special commands within `screen`
* `ctrl-a`: primes `screen` function for a character input which performs a special function
* `ctrl-a' then 'c': open new screen
* `ctrl-a' then `n`: move to next screen
* `ctrl-a' then `p`: move to previous screen
* `ctrl-a` then `2`: move to screen 2
* `ctrl-a' then `d`: disconnects from a screen (but processes continue to run)
* `ctrl-d`: kills active screen selection (terminates processes)

### tmux
Similar function to `screen`
`tmux new`: create new tmux session
`ctrl-b`: primes `tmuxz` for a character input which performs a special function

### Sharing screen sessions
Can be done in both `screen` and `tmux`
`tmate show-messages`: prints URLs that allow remote access for someone to initiate an ssh connection

# Using argparse
Step 1: `import argparse`
Step 2: Make a parser - `parser = argparse.Argumentparser()`
Step 3: Prime parser to tell it what might be on the command line
`parser.add_argument ()`
Step 4: Use it - tell it to go and parse what is on command line
`args = parser.parse_args(sys.argv)`
or
`args = parser.parse_args()

## Allowing argparse to read a file
`parser.add_argument(
	"file", type = argparse.Filetype(), default = sys.stdin,
	help = "The file to read")

Note it is just "file" not "--file". This makes it a positional argument which comes as the last argument
