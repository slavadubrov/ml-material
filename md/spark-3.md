@title[Spark: MLlib]
## Spark: MLlib

+++
@title[MLlib Data Types: Local Vectors]
<span style="color:gray; font-size:1em">MLlib Data Types: Local Vectors </span>
* Local Vectors:
    - stored on a single machine
    - integer-typed and 0-based indices
    - double-typed values

+++
@title[MLlib Data Types: Local Vectors]
<span style="color:gray; font-size:0.7em">MLlib Data Types: __Local Vectors__ </span>
- <span style="font-size:0.7em">Dense Vectors</span>
    + <span style="font-size:0.7em">backed by a double array representing its entry values</span>
- <span style="font-size:0.7em">Sparse Vectors</span>
    + <span style="font-size:0.7em">backed by two parallel arrays: indices and values</span>

```python
import numpy as np
from pyspark.mllib.linalg import Vectors

dv1 = np.array([1.0, 0.0, 3.0])
dv2 = [1.0, 0.0, 3.0]
dv3 = Vectors.dense([1.0, 0.0, 3.0])
sv1 = Vectors.sparse(3, [0, 2], [1.0, 3.0])

```

+++
@title[MLlib Data Types: Labeled point]
<span style="color:gray; font-size:1em">MLlib Data Types: __Labeled point__ </span>
- specialized local vector
- associated with a label/response
- used in supervised learning algorithms

```python
from pyspark.mllib.linalg import SparseVector
from pyspark.mllib.regression import LabeledPoint

pos = LabeledPoint(1.0, [1.0, 0.0, 3.0])
neg = LabeledPoint(0.0, SparseVector(3, [0, 2], [1.0, 3.0]))
```

+++
@title[MLlib Data Types: Local matrix]
<span style="color:gray; font-size:0.8em">MLlib Data Types: __Local matrix__ </span>
- <span style="font-size:0.8em">stored on a single machine</span>
- <span style="font-size:0.8em">stored in column-major order</span>
- <span style="font-size:0.8em">can be: __dense__ | __sparse__</span>
```python
from pyspark.mllib.linalg import Matrix, Matrices
dm = Matrices.dense(3, 2, [1, 2, 3, 4, 5, 6])
sm = Matrices.sparse(3, 2, [0, 1, 3], [0, 2, 1], [9, 6, 8])
```
@[2](Create a dense matrix ((1.0, 2.0), (3.0, 4.0), (5.0, 6.0)))
@[3](Create a sparse matrix ((9.0, 0.0), (0.0, 8.0), (0.0, 6.0)))

+++
@title[MLlib Data Types: Distributed matrix]
<span style="color:gray; font-size:1em">MLlib Data Types: __Distributed matrix__ </span>
- stored distributively in one or more RDDs
- long-typed row and column indices
- double-typed values

+++
@title[ML Pipelines]
<span style="color:gray; font-size:1em">ML Pipelines </span>
* provide a uniform set of high-level APIs built on top of DataFrames
* help users create and tune practical machine learning pipelines

![Image-Absolute](pics/pipeline-1.png)

+++
@title[ML Pipeline components]
<span style="color:gray; font-size:1em">ML Pipeline components </span>

* Transformers
* Estimators

![Image-Absolute](pics/ml-Pipeline.png)
