@title[Spark: Intro]
## Spark: Intro

+++
@title[Spark: Intro]

* Evaluation
    - First release in 2012
    - Today 2.1 version
* Written on Scala
* API for
    - Scala, Python, Java, R
* Where to develop
    - Spark-shell, InteliJ, Jupyter, Zeppelin, Databricks
* What you need for work with Spark
    - Cluster manager

+++
@title[Hadoop VS Spark]

<span style="color:gray; font-size:0.7em">Hadoop VS Spark </span>

![Image-Absolute](pics/HadoopVSSpark.png)

+++
@title[Hadoop Job Process]

<span style="color:gray; font-size:0.7em">Hadoop Job Process </span>

![Image-Absolute](pics/hadoop-job-process.png)

+++
@title[Spark Job Process: In memory]

<span style="color:gray; font-size:0.7em">Spark Job Process: In memory </span>

![Image-Absolute](pics/spark-job-process.png)

+++
@title[Fault tolerance]

<span style="font-size:1em; color:gray">__Fault tolerance__</span>
* __Hadoop__
    - Save data on HDFS in 3 copies
* __Spark__
    - Saving chain of calculation

+++
@title[Spark Stack]

<span style="color:gray; font-size:0.7em">Spark Stack </span>

![Image-Absolute](pics/spark-stack.png)

---
@title[Spark: Inside]
## Spark: Inside

+++
@title[Cluster managers]

__Cluster managers__

* Yarn
* Mesos

+++
@title[Spark Yarn]

<span style="color:gray; font-size:0.7em">Spark Yarn </span>

![Image-Absolute](pics/spark-yarn.png)

+++
@title[RDD]

<span style="color:gray; font-size:0.7em">RDD </span>

* Resilient Distributed Dataset
* Dataset, Distributed on executor’s
* How we can get it:
    - From files
        - sc.textFile(“path/to/file”)
    - From memory
        - sc.parallelize(list)
    - From other RDD

+++
@title[RDD Example]

<span style="color:gray; font-size:0.7em">RDD Example </span>
```python
a = range(100)
data = sc.parallelize(a)
data.take(5)
```

@[2](Create RDD from a list.)
@[3](Return first 5 elements from RDD: [0, 1, 2, 3, 4])

+++
@title[What is this “sc”?]

<span style="color:gray; font-size:0.7em">What is this “sc”? </span>
* SparkContext
* Main entry point for Spark functionality
```python
from pyspark import SparkContext, SQLContext
sc = SparkContext()
sqlContext = SQLContext(sc)
```

+++
@title[More Detailed SC Initialization]

<span style="color:gray; font-size:0.7em">More Detailed SC Initialization </span>

```python
from pyspark import SparkContext,SparkConf,SQLContext

conf = (SparkConf()
            .setMaster("local[*]")
            .setAppName("AppName")
            .set("spark.executor.memory", "4g")
            .set("spark.cores.max", "2"))

sc = SparkContext(conf=conf)

sqlCtx = SQLContext(sc)
```

+++
@title[Spark Operations]

<span style="color:gray; font-size:1em">Spark Operations </span>

![Image-Absolute](pics/spark-operations.png)

+++
@title[Spark Operations: Transfomations]

<p><span style="color:gray; font-size:1em">Spark Operations: Transfomations </span>
<p><span style="color:red; font-size:1em">LAZY! </span> | 
<span style="font-size:0.8em">Create new datasets from an existing one </span> |<span style="color:red; font-size:1em">LAZY! </span>
```scala
map
flatMap
mapPartitions
filter
join
union
distinct
reduceBykey
```

+++
@title[Spark Operations: Actions]

<p><span style="color:gray; font-size:1em">Spark Operations: Actions </span>
<p><span style="font-size:0.8em">Mechanism for getting results out of Spark </span>
```scala
reduce
collect
count
first
take
saveAsTextFile
```

---
@title[Spark: Inside 2]
## Spark: Inside 2

+++
@title[RDD flow]

<span style="color:gray; font-size:0.7em">RDD flow </span>

![Image-Absolute](pics/rdd-flow.png)

+++
@title[RDD flow: Perfomance trouble]

<span style="color:gray; font-size:0.7em">RDD flow: Perfomance trouble </span>

![Image-Absolute](pics/performance-trouble.png)

+++
@title[Solution 1]

<span style="color:gray; font-size:0.7em">Solution 1 – .collect() </span>

![Image-Absolute](pics/solution-1.png)

+++
@title[Solution 1: Out of memory]

<span style="color:gray; font-size:0.7em">Solution 1: Out of memory </span>

![Image-Absolute](pics/out-of-memory.png)

+++
@title[Solution 2]

<span style="color:gray; font-size:0.7em">Solution 2 – .persist() </span>

![Image-Absolute](pics/solution-2.png)

---
@title[Spark: Shared Data]

## Spark: Shared Data

+++
@title[Shared Data]

<span style="color:gray; font-size:0.7em">Shared Data </span>

![Image-Absolute](pics/shared-data.png)

+++
@title[Shared Data]

<span style="color:gray; font-size:1em">Shared Data </span>

* Variables that you want to share to all cluster;
* Shouldn’t be big;
* Two types:
    * Broadcast variables
    * Accumulators

+++
@title[Broadcast variables]

<p><span style="font-size:1em">__Broadcast variables__ </span>
<p><span style="color:red; font-size:1em">Immutable! </span>

```python
broadcast_var = sc.broadcast([1,2,3])
broadcast_var.value
```

+++
@title[Accumulators]

<p><span style="font-size:1em">__Accumulators__ </span>
<p><span style="color:red; font-size:1em">Not readable! </span>

```python
accum = sc.accumulator(0)
sc.parallelize([1,2,3,4]).foreach(lambda x: accum.add(x))
accum.value
```

---
@title[Spark: practice]
## Spark: practice

+++?code=scripts/spark_practice.py&lang=python&title=Spark: Practice

@[1-4](Import and initialization)
@[6](RDD Creation)
@[8](Take first element from RDD: 0)
@[10](Take first ten elements from RDD: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
@[12](Take all elements from RDD: [0, 1, 2, ... 99])
@[14-16](Map through elements: [0, 2, 4, ... 198])
@[18-20](Map through elements and filter them by condition: [0, 0, 2, 2, 4, 4, 6, 6, 8, 8 ...])
@[22-24](Get unique elements: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
@[26](Count elements)
@[28](Get first 5 maximum elements)
@[30](Get first 3 minimum elements)
@[32](Sum of elements with reduce())
@[34](Sum of elements with fold(): return sum + 100*(number_of_partitions+1))
@[36](Get number of partitions)
@[38](Count every unique element)
@[41-44](Count elements by key)
@[47-49](flatMap() example)
@[52-57](groupByKey() sum example)
@[60-63](reduceByKey() sum example)
@[66](Read text file)
@[70-74](WordCount example)
@[77-89](Cache examples)
@[92-100](Broadcast example)
@[102-105](Accumulator example)

---
@title[Spark: Some Experience]
## Spark: Some Experience

+++
@title[Big library initialization]
* You need to initialize big library in the cluster!
What best solution?

```python
.mapPartions(
    Initialization on the cluster;
    map(calculation in RDD)
)
```
