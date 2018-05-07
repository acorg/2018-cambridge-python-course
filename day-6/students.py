#!/usr/bin/env python

import pandas as pd
# import numpy as np

df = pd.read_excel('students.xlsx', 'Sheet1')

totalQuality = 0
countriesSeen = set()

for row in range(len(df)):
    rowData = df.loc[row]
    country = rowData['country']

    # if country == 'stop':
    #     break

    # if country in countriesSeen:
    #     continue

    if 'a' in country:
        countriesSeen.add(country)
        totalQuality += rowData['quality']
    # else:
    #     continue


print('Countries seen:', ', '.join(sorted(countriesSeen)))
print('Total qualiity =', totalQuality)
