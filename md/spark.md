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