from csv import reader
from pyspark.mllib.clustering import KMeans
#import KMeans from pyspark
from pyspark import SparkContext 
import numpy as np
import re

sc = SparkContext(appName="MySparkProg")
sc.setLogLevel("ERROR")
data = sc.textFile("hdfs://10.56.2.193:54310/user/cc/hw2-input/")
# use csv reader to split each line of file into a list of elements.
# this will automatically split the csv data correctly.
rdd = data.mapPartitions(lambda x: reader(x))
rdd = rdd.filter(lambda x: (re.match(r'07\/[0-9]{2}\/[0-9]{4}', x[5])))
crimes = rdd.map(lambda x: (x[7],1)).reduceByKey(lambda x,y: x+y).sortBy(lambda x: x[1], False).take(3)

print("The top 3 types of crime committed in July are as follows:")
print(crimes)
# How many crimes of type DANGEROUS WEAPONS were reported in the month of July?
rdd = data.mapPartitions(lambda x: reader(x))
rdd = rdd.filter(lambda x: ("DANGEROUS WEAPONS" in x[7]))
rdd = rdd.filter(lambda x: (re.match(r'07\/[0-9]{2}\/[0-9]{4}', x[5])))
print("There were %s crimes of type \'DANGEROUS WEAPONS\' committed in the month of July" % (rdd.count()))
