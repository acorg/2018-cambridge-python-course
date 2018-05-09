#!/bin/bash

case $# in
    0)
        # Write an error to standard error.
        echo "Hey, give me some files!!!" >&2
        exit 1
        ;;
esac

for file in "$@"
do
    case $file in
        *.wc)
            base=$(echo $file | sed 's/\.wc$//')
            newfile=$base.new

            if test -f $newfile
            then
                echo "New file $newfile already exists. Skipping." >&2
            else
                echo hello > $newfile
            fi
            ;;
        *)
            echo "Unrecognized filename $file" >&2
            ;;
    esac
done
