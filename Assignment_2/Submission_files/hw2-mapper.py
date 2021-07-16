#!/usr/bin/env python
from csv import reader
import sys

# skip first line
next(sys.stdin)
# boro dictionary layout
# boroDict[boro] = [crimeTotal, crimeList[]]
boroList = []
i = 0

for line in reader(sys.stdin):
    boro, crime = (line[13].strip(), line[7].strip())
    if not boro or not crime:
        continue
    print("%s\t%s\t%s" % (boro, crime, 1))
