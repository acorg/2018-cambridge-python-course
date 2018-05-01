#!/usr/bin/env python3

import argparse
from Bio import SeqIO


def analyze1(seq, windowSize):
    print('The sequence is', seq, 'the window size is',
          windowSize, 'and the sequence has length', len(seq))
    start = 0
    stop = start + windowSize
    length = len(seq)

    def countGs(s):
        return s.count('G')

    while stop < length:
        window = seq[start:stop]
        print('  The next window is', window)
        print('  The G count is', countGs(window))
        start += windowSize
        stop += windowSize


def analyze2(seq, windowSize):
    print('Fake analysis!')


parser = argparse.ArgumentParser(
    description='Scrip to to do a windowed analysis.')

parser.add_argument(
    '--analyzeFunction', default='analyze1',
    choices=('analyze1', 'analyze2'),
    help='The sliding window size.')

parser.add_argument(
    '--windowSize', '-w', type=int, default=10,
    help='The sliding window size.')

parser.add_argument(
    '--verbose', action='store_true', default=False,
    help='If given print extra helpful output.')

args = parser.parse_args()

if args.verbose:
    print("Hey, welcome to version 0.0.0.1 of our "
          "wonderful program...")

if args.analyzeFunction == 'analyze1':
    analyzeFunc = analyze1
else:
    analyzeFunc = analyze2

for record in SeqIO.parse('test.fastq', 'fastq'):
    sequence = str(record.seq)
    analyzeFunc(sequence, args.windowSize)
