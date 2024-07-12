from pyspark import SparkContext
sc = SparkContext("local", "AppName")

a = list("A","B","C")
aRDD = sc.parallelize(a)
print("HIIIIIIIIIIIIII" ,aRDD.count)

'''
    scala> val brands = List("Tesla", "Ford", "GM")
    brands: List[String] = List(Tesla, Ford, GM)

    scala> val brandsRDD = sc.parallelize(brands)
    brandsRDD: org.apache.spark.rdd.RDD[String] = ParallelCollectionRDD[0] at parallelize at <console>:24

    scala> brandsRDD.count
    res0: Long = 3

'''