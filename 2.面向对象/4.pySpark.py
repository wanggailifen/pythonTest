# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyspark

from pyspark import SparkConf, SparkContext, RDD

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

sc = SparkContext(conf=conf)

print(sc.version)
#
rdd1 = sc.parallelize([1, 2, 3, 4, 5])


# rdd2: RDD = sc.parallelize("ABCDEFG")
#
# print(rdd1.collect())
# print(rdd2.collect())

# rdd3 = sc.textFile("test/123.txt")
# print(rdd3.collect())

def func(data):
    return data * 10


result1 = rdd1.map(func)

print(result1.collect())
sc.stop()
