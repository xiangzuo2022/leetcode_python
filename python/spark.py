## Spark Application - execute with spark-submit

## Imports
from pyspark import SparkConf, SparkContext
from operator import add

## Module Constants
APP_NAME = "populargram"

## Closure Functions

## Main functionality

def main(sc):
    text = sc.textFile("article.txt")
    def tokenize(text):
        return text.split()
    words = text.flatMap(tokenize)
    wc = words.map(lambda x:(x,1))
    counts = wc.reduceByKey(add)
    counts.saveAsTextFile("wc2")

if __name__ == "__main__":
    # Configure Spark
    conf = SparkConf().setAppName(APP_NAME)
    conf = conf.setMaster("local[*]")
    sc   = SparkContext(conf=conf)

    # Execute Main functionality
    main(sc)

    sc.stop()