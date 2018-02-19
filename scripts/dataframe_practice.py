from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df = spark.read \
	.format("csv") \
	.option("header", "true") \
	.load("../path/to/file.csv")

import pyspark.sql.functions as func
spark_df.groupBy("auto_number") \
    .agg(func.max("compensated"), func.sum("compensated")) \

dfjoin = spark_df.groupBy("auto_number") \
    .count()

spark_df \
     .join(dfjoin, spark_df["auto_number"] == dfjoin["auto_number"], "left") \
     .drop(dfjoin["auto_number"])

dftmp = spark.read.json("../../data/employee.json")
dftmp.write.save("../../data/namesAndAges.parquet")
spark.read.parquet("../../data/namesAndAges.parquet")

spark_df.createOrReplaceTempView("spark_df")
sqlDF = spark.sql("SELECT * FROM people")