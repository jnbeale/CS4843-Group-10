#!/usr/bin/env python
import sys

maxCrimes = 0
maxBoro = None
currBoro = None
currCnt = 0
boro = None
crimeList = []
maxCrimeList = []
for line in sys.stdin:
    line = line.strip()
    boro, crime, crimeCnt = line.split('\t', 2)
    if not boro or not crime:
        continue
    try:
        crimeCnt = int(crimeCnt)
    except ValueError:
        continue

    if currBoro == boro:
        currCnt += crimeCnt
        if crime not in crimeList:
            crimeList.append(crime)
    else:
        if currBoro:
            if currCnt > maxCrimes:
                maxCrimes = currCnt
                maxBoro = currBoro
                maxCrimeList = crimeList
            print("%s\t%s" % (currBoro, currCnt))
        currCnt = crimeCnt
        currBoro = boro
        crimeList = []
if currBoro == boro:
    print("%s\t%s" % (currBoro, currCnt))
print("%s has the highest crime rate with %s crimes committed" % (maxBoro, maxCrimes))
print("Crimes include %s" % (crimeList))
    # input test code
    #print("BORO")
    #print(boro)
    #print("CRIME")
    #print(crime)
    #for curr in boroList:
    #    firstTime = True
    #    if boro == curr['name']:
    #        firstTime = False
    #        break;
        
    #if firstTime == True:
    #    boroDict = {'name': boro, 'crimeTotal': 1, 'crimeList': [crime]}
    #    boroList.append(boroDict)
    #    print("Added %s" % boroDict['name'])
    #    continue
    # find the boro in the list
    #for curr in boroList:
    #    if boro is curr['name']:
    #        curr['crimeTotal'] = curr['crimeTotal']+1
    #        if crime not in curr['crimeList']:
    #            curr['crimeList'].append(crime)
#max = 0
#maxBoro = ''
#for boro in boroList:
#    if max == 0:
#        max = boro['crimeTotal']
#        maxBoro = boro['name']
#        continue
#    if boro['crimeTotal'] > max:
#        max = boro['crimeTotal']
#        maxBoro = boro['name']
#    print("%s had %d crimes total" % (boro['name'], boro['crimeTotal']))
#print("The most crime is in %s with %d crimes" % (maxBoro, max))
