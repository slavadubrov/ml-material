@title[Introduction]

# Introduction

+++
@title[Machine Learning Algorithms]

## Machine Learning Algorithms

* Supervised Learning
* Unsupervised Learning
* Semi-Supervised Learning

+++
@title[Supervised Learning]

## Supervised Learning

* __Classification__: A classification problem is when the output variable is a category, such as “disease” and “no disease”.
* __Regression__: A regression problem is when the output variable is a real value, such as “dollars” or “weight”.

+++
@title[Formalization]

## Formalization

* __X__ – set of objects
* __T__ – set of values ​​of the target variable.

<p> A training sample of objects is given</p>
`$$ X = \left( x_1, ..., x_N \right) ^T , x_i \in  X $$`

<p> and the corresponding classes</p>
`$$ T = \left( t_1, ..., t_N \right) ^T , t_i \in  T $$`

<p> It is required to find a function </p>
`$$ y^*(x) : X \rightarrow T $$`

<p> allowing for the most accurate x ∈ X the most accurate prediction of the corresponding t ∈ T </p>

+++
@title[Target variable]

## Target variable

* `\( T = \left\{  C_1,...,C_K \right\} \)` - the classification problem in K disjoint classes
* `\( T = \left[  a,b \right] \subset R \)` - the regression problem

+++
@title[How to solve?]

## How to solve?

* __Model selection__: advance the hypothesis about the model - a family of parametric functions of the form which could solve problem
`$$ Y=\left\{ y\left( x,\theta  \right) :X\times \Theta  \rightarrow T \right\} $$`
* __Learning/Inference__: using the learning algorithm choose the best parameters of the model `\( \Theta^* \)`
`$$ A(X,T) : (X,T)^N \rightarrow  Y $$`
* __Decision making__: using the obtained model `\( y^ ∗(x) = y(x,\theta ^∗) \)` classify unknown objects


