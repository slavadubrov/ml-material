@title[Directions]

## Directions

+++
@title[Supervised]

* **Supervised learning** problems - applications in which the training data comprises examples of the input vectors along with their corresponding target vectors
<span style="font-size:0.8em">
    * Classification
    * Regression
</span>

+++
@title[Unsupervised]

* **Unsupervised learning** problems - the training data consists of a set of input vectors x without any corresponding target values
<span style="font-size:0.8em">
    * Clustering
    * Density estimation
    * Dimensionality reduction
    * Anomaly detection
</span>

+++
@title[Reinforcement learning]

* **Reinforcement learning** is concerned with the problem of finding suitable actions to take in a given situation in order to maximize a reward
<span style="font-size:0.8em">
    * Here the learning algorithm is not given examples of optimal outputs, in contrast to supervised learning, but must instead discover them by a process of trial and error.
    * Typically there is a sequence of states and actions in which the learning algorithm is interacting with its environment.
</span>

+++
@title[Recommender systems]

* **Recommender systems**  estimate a utility function that automatically predicts how a user will like an item. Based on:
<span style="font-size:0.8em">
    * Past behavior
    * Relations to other users
    * Item similarity
    * Context
</span>

---
@title[Supervised learning]

## Supervised learning

+++
@title[Classification]

* **Classification**
	* The aim is to assign each input vector to one of a finite number of discrete categories
		* Example: the digit recognition

* **Regression**
	* The aim is to predict for each input vector some continuous variable
		* Example: price of the apartments prediction

---
@title[Performance Metrics. Classification]

## Performance Metrics. Classification

+++
@title[Confusion Matrix]

<span style="color:gray; font-size:0.7em">Confusion Matrix </span>

![](pics/confusion-matrix.png)

+++
@title[Accuracy, Precision, Recall]

<span style="color:gray; font-size:0.7em">Accuracy, Precision, Recall </span>

![](pics/confusion-matrix-2.png)

+++
@title[When to use Precision and When to use Recall?]

### When to use Precision and When to use Recall?

* **Precision** is about being precise. So even if we managed to capture only one cancer case, and we captured it correctly, then we are 100% precise.

* **Recall** is not so much about capturing cases correctly but more about capturing all cases that have “cancer” with the answer as “cancer”. So if we simply always say every case as “cancer”, we have 100% recall.

+++
@title[F-measure]

### Balanced Precision/Recall metrics

* **F-measure** is Harmonic mean of Precision and Recall.
$$ F_{ \beta  } = \left( 1 + { \beta  }^{ 2 } \right) \cdot \frac { Precision\cdot Recall }{ { \beta  }^{ 2 }\cdot Precision + Recall } $$
* **F1-measure**
$$	F_{ 1 } = 2 \cdot \frac { Precision\cdot Recall }{ Precision + Recall } $$

+++
@title[Harmonic Mean]

#### Harmonic mean

**Harmonic mean** is kind of an average when x and y are equal. But when x and y are different, then it’s closer to the smaller number as compared to the larger number.

![](pics/harmonic-mean.png)

+++
@title[TPR/FPR]

### TPR/FPR

* **True Positive Rate (TPR)**
$$ TPR=\frac { TP }{ TP+FN } $$
* **False Positive Rate (FPR)**
$$ FPR=\frac { FP }{ FP+TN } $$

+++
@title[Receiver Operating Characteristics (ROC)]

#### Receiver Operating Characteristics (ROC)
#### Area Under the Curve (AUC)

![](pics/roc.png)

+++
@title[AUC]

![Video](https://youtube.com/embed/OAl6eAyP-yo)

---
@title[Performance Metrics. Regression]

## Performance Metrics. Regression

+++
@title[MSE/MAE]

* **Mean Squared Error**
$$ MSE=\frac { 1 }{ N } \sum { ( y(x_i)-t_i) ^ 2 } , \quad RMSE=\sqrt { MSE } $$
* **Mean Absolute Error**
$$ MAE=\frac { 1 }{ N } \sum { | y(x_i)-t_i | } , \quad RMAE=\sqrt { MAE }  $$

+++
@title[R2 Metric]

* The total sum of squares:
$$ SS_tot=\sum _{i}(y_i - {\bar {y}})^2 $$
* The regression sum of squares, also called the explained sum of squares:
$$ { SS_{\text{reg}}=\sum _{i}(f_{i}-{\bar {y}})^{2},} SS_{\text{reg}}=\sum _{i}(f_{i}-{\bar {y}})^{2}, $$
* The sum of squares of residuals, also called the residual sum of squares:
$$ { SS_{\text{res}}=\sum _{i}(y_{i}-f_{i})^{2}=\sum _{i}e_{i}^{2}\,} {\displaystyle SS_{\text{res}}=\sum _{i}(y_{i}-f_{i})^{2}=\sum _{i}e_{i}^{2}\,} $$
* The coefficient of determination
$$ { R^{2}\equiv 1-{SS_{\rm {res}} \over SS_{\rm {tot}}}.\,} R^{2}\equiv 1-{SS_{\rm {res}} \over SS_{\rm {tot}}}.\, $$