from pyspark import SparkContext, SQLContext

sc = SparkContext()
sqlContext = SQLContext(sc)

rdd_1 = sc.parallelize(xrange(100))

rdd_1.first()

rdd_1.take(10)

rdd_1.collect()

(rdd_1
    .map(lambda x: x * 2)
    .collect())

rdd_2 = (rdd_1
    .map(lambda x: x / 2)
    .filter(lambda x: x % 2 == 0))

(rdd_2
    .distinct()
    .take(10))

rdd_2.count()

rdd_2.top(5)

rdd_2.takeOrdered(3)

rdd_1.reduce(lambda a, b: a + b)

rdd_1.fold(100, lambda a, b: a + b)

rdd_1.getNumPartitions()

rdd_2.countByValue()

# countByKey()
rdd_key_value = (rdd_1
    .map(lambda x: ((x / 4)**3, x)))
rdd_key_value.take(10)
rdd_key_value.countByKey()

# flatMap()
(rdd_1
    .flatMap(lambda x: (x, (x / 4)**3))
    .take(10))

# groupByKey()
rdd_3 = sc.parallelize([("a", 10), ("b",20), ("b", 10)])
rdd_3.take(5)
(rdd_3
    .groupByKey()
    .mapValues(lambda x: sum(x))
    .collect())

# reduceByKey()
from operator import add
(rdd_3
    .reduceByKey(add)
    .take(5))

# Read txt
rdd_txt = sc.textFile("../../data/Sherlock.txt")
rdd_txt.take(20)

# WordCount
(rdd_txt
    .flatMap(lambda x: x.strip().split())
    .map(lambda x: (x.lower(), 1))
    .reduceByKey(add)
    .take(10))

# Cache
rdd_cache = (rdd_txt
    .flatMap(lambda x: x.strip().split())
    .persist())
(rdd_cache
    .map(lambda x: (x.lower(), 1))
    .reduceByKey(add)
    .take(10))
(rdd_cache
    .count())
(rdd_cache
    .map(lambda x: x.lower())
    .distinct()
    .count())

# Broadcast
very_important_dic = {"a": 12, "b": 23, "c":34}
vid_br = sc.broadcast(very_important_dic)
vid_br.value
(rdd_3
    .map(lambda x: very_important_dic[x[0]])
    .collect())
(rdd_3
    .map(lambda x: vid_br.value[x[0]])
    .collect())

# Accumulator
acc_1 = sc.accumulator(0)
rdd_3.foreach(lambda x: acc_1.add(x[1]))
acc_1