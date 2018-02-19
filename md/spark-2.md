@title[Spark: Dataframes]
## Spark: Dataframes

+++
@title[Dataframe]
<span style="color:gray; font-size:1em">Dataframe </span>

Distributed collection of data organized into named columns;
Higher-level abstraction in Spark;
Unchangeable;
It is created using SparkSession.

+++
@title[Dataframe: Initialization]
<span style="color:gray; font-size:1em">Dataframe: Initialization </span>

```python
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
```

+++
@title[DataFrames are faster]

<p><span style="font-size:1em">__DataFrames are faster__</span>
<p><span style="color:gray; font-size:0.7em">Because of the optimization, they tend to outperform RDDs </span>

![Image-Absolute](pics/dataframe-performance.png)

+++
@title[Creating a DataFrame]
<span style="color:gray; font-size:1em">Creating a DataFrame </span>

* From RDD (.toDF () <=> .rdd)
* From other DataFrames (after transformations)
* From Python collections
* From files
* From Pandas DataFrames

+++
@title[Creating a DataFrame: Examples]
<span style="color:gray; font-size:1em">Creating a DataFrame: Examples </span>
```python
data = [('Batgirl', 21), ('Batman', 32)]
df = sparkSession.createDataFrame(data, ['name', 'age'])

text_df = spark.read.text("../path/to/file.txt")

import pandas as pd
pandas_df = pd.read_csv("path/to/file.csv")
spark_df = spark.createDataFrame(pandas_df)
```
@[1-2](Creating a DataFrame from Python list)
@[4](Creating a DataFrame from text file)
@[6-8](Creating a DataFrame from Pandas DataFrame)

+++
@title[Row Object]
<span style="font-size:1em">__Row Object__ </span>
* Each line in the DataFrame is a Row Object
```python
from pyspark.sql import Row
row = Row(name="Alice", age=11)
print(row['name'])
```
@[3](Row fields of objects can be accessed by attributes)

+++
@title[DataFrame Flow]

<p><span style="font-size:1em">__DataFrame Flow__</span>
* Two types of operations:
    - transformations
    - actions
* Persist (cache) DFs into memory or drive

![Image-Absolute](pics/dataframe-flow.png)

+++
@title[DataFrame: Selection 1]
<span style="font-size:1em">__Select and return DataFrame__ </span>
```python
spark_df.select('*')
spark_df.select('auto_number')
from pyspark.sql.functions import col
spark_df.select(col('auto_number'))
```
@[1](Select Dataframe with all columns)
@[2](Select Dataframe with one column)
@[3-4](Select Dataframe with one column)

+++
@title[DataFrame: Selection 2]
<span style="font-size:1em">__Select and return DF column__ </span>
```python
spark_df.auto_number
spark_df['auto_number']
```

+++
@title[DataFrame: Transformations]
<span style="font-size:1em">__DataFrame: Transformations__ </span>
```python
df.filter(func)
df.dictinct()
df.orderBy()
df.sort()
df.drop()
```

+++
@title[DataFrame: Actions]
<span style="font-size:1em">__DataFrame: Actions__ </span>
```python
df.collect()
df.take(5)
df.count()
df.show()
df.describe()
```

+++
@title[DataFrame: User Defined Function (UDF)]
<span style="font-size:1em">__DataFrame: User Defined Function (UDF)__ </span>
```python
(spark_df
    .filter(spark_df["id"] >= 15)
    .show(5))    
```

+++
@title[DataFrame: User Defined Function (UDF)]
<span style="font-size:1em">__DataFrame: User Defined Function (UDF)__ </span>
```python
(spark_df
    .filter(len(spark_df["auto_brand"]) >= 15)
    .show(5))    
```

+++
@title[DataFrame: User Defined Function (UDF)]
<span style="font-size:1em">__DataFrame: User Defined Function (UDF)__ </span>
```python
from pyspark.sql.functions import idf
from pyspark.sql.types import BooleanType
u_f = udf(lambda s: len(s) >= 15, BooleanType())
(spark_df
    .filter(u_f(spark_df["auto_brand"]))
    .show(5))    
```

+++
@title[GroupedData and Merge Functions]
<span style="font-size:1em">__GroupedData and Merge Functions__ </span>
```python
groupBy(*cols)
agg(*exprs)
count()
avg()
df1.join(df2)
df1.unionAll(df2)
```

+++
@title[DataFrame: Parquet]

<p><span style="font-size:1em">__DataFrame: Parquet__</span>

![Image-Absolute](pics/parquet.jpg)

+++
@title[DataFrame: SQL support]
<p><span style="font-size:1em">__DataFrame: SQL support__</span>
```python
df.createOrReplaceTempView("people")

sqlDF = spark.sql("SELECT * FROM people")
sqlDF.show()
```