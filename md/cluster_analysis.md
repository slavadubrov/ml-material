@title[Cluster analysis]

# Cluster analysis

+++
@title[Metrics]

## Metrics

+++
@title[Metrics]

* __Silhouette__: 
`$$ s(i)\quad =\quad \frac { b(i)\quad -\quad a(i) }{ \max { \left\{ a(i),b(i) \right\}  }  }  $$`
	* b(i) - distance to neighboring cluster
	* a(i) - distance to my cluster
* smaller `\( a_i \)` is better
* `\( s_{ i }\rightarrow 1\quad \Rightarrow \quad a(i)\ll b(i)  \)`


+++
@title[K-means clustering algorithm]

## K-means clustering algorithm

* Input: K, set of points `\( { x }_{ 1 }..{ x }_{ n } \)`
* Place centroids `\( c_1..c_k \)` at random locations
* Repeat until convergence:
	* for each point `\( x_i \)`:
		* find nearest centroid `\( c_j \)` based on `\( D(x_i,c_j) \)`
		* assign the point `\( x_i \)` to cluster _j_.
	* for each cluster `\( j = 1..K \)`: `\( x_i \)`:
		`$$ c_{ j }(a)=\frac { 1 }{ n_{ j } } \sum _{ x_{ i }\rightarrow c_{ j } }{ x_{ i }(a) } \quad for\quad a=1..d $$`
		* new centroid `\( c_j = \)` mean of all points `\( x_i \)` assigned to cluster _j_ in previous step.
* Stop whr none of the cluster assignements change.

+++
@title[K-medians clustering algorithm]

## K-medians clustering algorithm

* like K-means, but instead of calculating means use the median.
 
## Distances

* Euclidean distance (between __p__ and __q__): `$$ d(p,q)\quad =\quad \sqrt { \sum _{ i=1 }^{ n }{ { \left( { q }_{ i }-{ p }_{ i } \right)  }^{ 2 } }  }  $$`

* Manhattan (Hamming) distance: `$$ d(p,q)\quad =\quad \sum _{ i=1 }^{ n }{ \left| { p }_{ i }-{ q }_{ i } \right|  }  $$`

* Cosine distance: `$$ cos\theta \quad =\quad \frac { A\cdot B }{ \left\| A \right\| \left\| B \right\|  } =\frac { \sum _{ i=1 }^{ n }{ { A }_{ i }\times { B }_{ i } }  }{ \sqrt { \sum { { A }_{ i }^{ 2 } }  } \sqrt { \sum { { B }_{ i }^{ 2 } }  }  }  $$`

