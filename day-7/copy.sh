#!/bin/bash

case $# in
    0)
        # Write an error to standard error.
        echo "Hey, give me some files!!!" >&2
        exit 1
        ;;
esac

for i in "$@"
do
    cp $i $i.orig
done
