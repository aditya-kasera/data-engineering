# from pyspark.sql import SparkConf, SparkSession
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName('Map_and_filter').setMaster("local[*]")
spark = SparkContext(conf = conf)

n = [1,2,3,4,5]
rdd = spark.parallelize(n)

sq_rdd = rdd.map(lambda x: x * x)

filtered_rdd = sq_rdd.filter(lambda x: x > 16)

res = filtered_rdd.collect()
print(res)

spark.stop()