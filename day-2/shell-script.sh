#!/bin/bash -e

a=4

# set +e
cat lsklksjljsjs
# set -e


# Here is a comment......
echo "Hello a is $a"


cat lskjslkjsks >output 2>errors

status=$?

# if test -s errors
if [ -s errors ]
then
    echo "The error file is not empty!" >&2
fi

if [ $status -ne 0 ]
then
    echo "There was an error!" >&2
    exit 1
fi
