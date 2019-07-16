[var_biased]: images/var_biased.png
[var_unbiased]: images/var_unbiased.png
[cov]:images/cov.png
# Statistics Assignment 1

## 1. Difference between Normalization Constants in Variance calculations

There are two slightly different formulas for the estimation of the variance of a population based on a selected sample. One formula uses the sample variance which is the sum of squared distances from the mean. The formula is shown below:

![var_biased]

where S is the standard deviation

The problem with this formula is that it susceptible to sampling bias which is the phenomenon in which certain important members or section of the population are either underrepresented or overrepresented in the sampling. For example if one were to attempt to find the average weight of blue fin tuna in the oceans, and the samples were gathered from only one part of the world, that will exclude the other members of the bluefin tuna population which For large samples the variance is an adequate estimator, but for small samples, it there tends to be a large difference between the sample variance and the expected variance. 

The approximation of the variance which is 

![var_unbiased]

however is unbiased. The explanation and proof for this can be found [here](http://wikipedia.org/wiki/Bias_of_an_estimator)

## 2. How would on calculate the Covariance Matrix
The covariance matrix is used to measure how the variables of a multivaritate signal or sample relate to each other. 

For a signal X = [x1, x2, ..........., xn] where n is the number of features/ variables of x, Suppose we have m examples of m, the covariance matrix will take the form 

|  	| x1 	|  x2	| ... 	|..  	| xn|
|-- |---	|---	|---	|---	|---|
|  	x1|  1	|  cov(x1, x2)	|cov(x1, ...)  	|  cov(x1, ...)	| cov(x1, xn) |
|  x2	|cov(x2, x1)  	|  1	|  	|  	| cov(x1, xn)|
|  ...	|  cov(..., x1)	| cov(..., x2) 	| 1 	|  	|cov( ... , xn)|
|  ...	|cov(..., x1)  	|  cov(..., x2)	|  	| 1 	|cov( ... , xn)|
|  xn	|  cov(xn, x1)	| cov(xn, x2) 	|  	|  	|1|

The properties of the Covariance matrix are listed below:

* they are symmetric ie for every A=transponse(A) for matrix A
* they are hessian

Using these properties, we can chose to calculate only the pairwise covariances ie, (x1, x2)(x,1,x3) etc. These do not need to be stored in a matrix, they can be smartly stored in a multimap or multikey dictionary and return in a matrix form when requested. The formula for covariance between two variables is shown below:

![cov]

Since cov(x,x)=1, the diagonals of the matrix are all 1 and need not be calculated
