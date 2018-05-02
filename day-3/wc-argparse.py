#!/usr/bin/env python

import sys
import argparse


def wc(countLines, countWords, countChars, fp):
    lines = words = chars = 0

    for line in fp:
        if countLines:
            lines += 1
        if countWords:
            words += len(line.split())
        if countChars:
            chars += len(line)

    return lines, words, chars


parser = argparse.ArgumentParser(
    description='Script to to do a windowed analysis.')

parser.add_argument(
    'file', type=argparse.FileType(), default=sys.stdin, nargs='?',
    help='The file to read (default stdin).')

parser.add_argument(
    '-l', action='store_true', default=False,
    help='If given only print the line count.')

parser.add_argument(
    '-w', action='store_true', default=False,
    help='If given only print the word count.')

parser.add_argument(
    '-c', action='store_true', default=False,
    help='If given only print the character count.')

args = parser.parse_args()


# Ask for all possible output if we weren't given
# any of -l, -w, -c.
if not (args.l or args.w or args.c):
    args.l = args.w = args.c = True

lines, words, chars = wc(args.l, args.w, args.c, args.file)

if args.l:
    print(lines)

if args.w:
    print(words)

if args.c:
    print(chars)
