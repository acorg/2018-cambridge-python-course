#!/bin/bash

PATH=/tmp:.:/usr/bin:/bin

case $# in
    0)
        # Write an error to standard error.
        echo "Hey, give me some files!!!" >&2
        exit 1
        ;;
esac

for i in "$@"
do
    lineCount=$(wc -l < $i)
    echo $lineCount > $i.wc
    echo "File $i has $lineCount lines"
done > LINE-COUNT-SUMMARY
