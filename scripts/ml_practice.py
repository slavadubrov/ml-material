from pyspark.mllib.regression import LabeledPoint, LinearRegressionWithSGD, LinearRegressionModel

data = sc.parallelize([
     LabeledPoint(4.0, [0.0]),
     LabeledPoint(5.0, [1.0]),
     LabeledPoint(6.0, [2.0]),
     LabeledPoint(7.0, [3.0])
])

model_1 = LinearRegressionWithSGD.train(data)
model_1.predict([1])

model_2 = LinearRegressionWithSGD.train(data, intercept=True)
model_2.predict([2])



from pyspark.ml.classification import LogisticRegression

training = spark.read.format("libsvm").load("scripts/sample_libsvm_data.txt")
lr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)
lrModel = lr.fit(training)



from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import HashingTF, Tokenizer

training = spark.createDataFrame([
    (0, "a b c d e spark", 1.0),
    (1, "b d", 0.0),
    (2, "spark f g h", 1.0),
    (3, "hadoop mapreduce", 0.0)
], ["id", "text", "label"])

test = spark.createDataFrame([
    (4, "spark i j k"),
    (5, "l m n"),
    (6, "spark hadoop spark"),
    (7, "apache hadoop")
], ["id", "text"])

tokenizer = Tokenizer(inputCol="text", outputCol="words")
hashingTF = HashingTF(inputCol=tokenizer.getOutputCol(), outputCol="features")
lr = LogisticRegression(maxIter=10, regParam=0.001)
pipeline = Pipeline(stages=[tokenizer, hashingTF, lr])

model = pipeline.fit(training)

prediction = model.transform(test)