#!/usr/bin/env python2.7
from csv import reader
from collections import Counter
from operator import itemgetter
import sys
total_crimes = 0
word2count = {}
# skip first line (the header)
next(sys.stdin)
for line in reader(sys.stdin):
    boro, crime = (line[13].strip(), line[7].strip())
    if not boro or not crime:
       continue
    # 1. What is the total number of crimes reported in that location ? (read number of lines)
    crimes = crime.split()
    for r in crime:
        if total_crimes == 0:
            total_crimes += 1
        else:
            total_crimes += 1
    print(f'the total number of crimes reported in that location: {total_crimes}')
    # other way count() function:
    # data = sys.stdin.readlines()
    # total_crime = data['OFNS_DESC'].count()
    #print ('Count of crimes in NY: ' + str(total_crime))

    # 2. Where is most of the crime happening in New York?
    where = boro.split()
    counter = Counter(where)
    most_frequent = counter.most_common(1)
    print('the most of the crime happening in New York: ' + most_frequent[0][0])

    # 3. What types of crime are happening in that location (show unique crime types) ?

    word, count = crime.split('\t', 1)
    try:
        count = int(count)
        word2count[word] = word2count.get(word, 0) + count

    except ValueError:
        pass

    sorted_word2count = sorted(word2count.items(), key=itemgetter(0))

    for word, count in sorted_word2count:
        print('%s\t%s' % (word, count))


