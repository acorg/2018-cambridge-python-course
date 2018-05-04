#!/usr/bin/env python

import sys


class FastaCollection():

    def __init__(self):
        self.sequences = {}

    def addSequence(self, id, sequence):
        pass

    def __len__(self):
        pass

    def hasId(self, id):
        """Return True if we are holding a sequence with id 'id'."""
        pass


fc = FastaCollection()


for line in sys.stdin:
    if line.startswith('>'):
        id = line[1:-1]
    else:
        fc.addSequence(id, line[:-1])
