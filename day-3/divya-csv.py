#!/usr/bin/env python

import csv
import sys

sitesOfInterest = {19, 33, 120, 311}

with open('table3_subs_edit.csv') as csvfile:
    aaReader = csv.reader(csvfile)
    lineNumber = 0
    for row in aaReader:
        lineNumber += 1

        # Make a list of the non-empty fields because the input contains
        # many trailing empty fields from the Excel export.
        nonEmptyFields = []
        for field in row:
            # Remove surrounding whitespace from the field.
            field = field.strip()
            # Change 'del' into '-' for easier subsequent processing.
            field = field.replace('del', '-')
            if field != '':
                nonEmptyFields.append(field)

        nFields = len(nonEmptyFields)
        if nFields < 2:
            print('Found a line without at least 2 fields.')
            sys.exit(1)

        # The first two fields are the strain names. They shouldn't be the
        # same.
        if row[0] == row[1]:
            if nFields == 2:
                print('On line %d, both ids are %s but there are no '
                      'mutations.' % (lineNumber, row[0]),
                      file=sys.stderr)
            else:
                print('On line %d, both ids are %s and there are %d '
                      'extra fields: %s.' % (
                          lineNumber, row[0], nFields - 2, ', '.join(row[2:])),
                      file=sys.stderr)
                sys.exit(1)

        seq1 = nonEmptyFields.pop(0)
        seq2 = nonEmptyFields.pop(0)

        # Print mutations at the sites we're interested in.
        for field in nonEmptyFields:
            if len(field) < 3:
                print('On line', lineNumber, 'there is a too-short field',
                      field, file=sys.stderr)
                sys.exit(1)
            aa1 = field[0]
            aa2 = field[-1]

            try:
                site = int(field[1:-1])
            except ValueError:
                print('On line %s there is an unparseable field %r.'
                      % (lineNumber, field), file=sys.stderr)

            if site in sitesOfInterest:
                print('%s vs %s: Change from %s to %s at site %d'
                      % (seq1, seq2, aa1, aa2, site))
