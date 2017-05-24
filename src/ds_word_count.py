# -*- coding: UTF-8 -*-

import os
import findspark
home=os.getenv("HOME")
findspark.init(os.path.join(home,"Downloads/spark-2.0.0-bin-hadoop2.7"))

import pyspark
from operator import add

myConf=pyspark.SparkConf()
spark = pyspark.sql.SparkSession.builder\
    .master("local")\
    .appName("myApp")\
    .config(conf=myConf)\
    .getOrCreate()
    


wc = spark.sparkContext.textFile("ds_spark_wiki.txt")\
    .map(lambda x: x.replace(',',' ').replace('.',' ').replace('-',' ').lower())\
    .map(lambda x:x.split())\
    .map(lambda x:[(i,1) for i in x])

for e in wc.collect():
    print e
