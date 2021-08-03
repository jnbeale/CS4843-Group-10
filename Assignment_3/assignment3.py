from csv import reader
from pyspark.mllib.clustering
import KMeans from pyspark
import SparkContext
import numpy as np

sc = SparkContext(appName="MySparkProg")
sc.setLogLevel("ERROR")
rdd = sc.textFile("hdfs://ipaddr:54310/hw2-input/")
# use csv reader to split each line of file into a list of elements.
# this will automatically split the csv data correctly.
rdd = rdd.mapPartitions(lambda x: reader(x))

# using filter with column condition (crimes in month of july)
rdd = rdd.filter(rdd.RPT_DT == "july")

# perform sum all the int values for each unique keys
rdd = rdd.reduceByKey(lamda x,y: x+y)

#function grab top 3
rdd = rdd.map(lamda x: (x[1], x[0])).sortByKey(False).take(3)

#print out
print("Top 3 crime types that were reported in the month of July are:")

