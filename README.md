# Breast cancer detection with KNN algorithm 

# K-Nearest Neighbour Classification
In pattern recognition, the K-Nearest Neighbor algorithm (K-NN) is a non-parametric method used
for classification and regression. In both cases, the input consists of the K closest training examples in the feature
space. K-NN is a type of instance-based learning.
In K-NN Classification, the output is a class membership. Classification is done by a majority vote of
neighbours. If K = 1, then the class is single nearest neighbour [6]. 

![](knn.png) [Fig 1.]

A test sample classification is shown in the above Fig 1. Consider the test sample is a big dot located inside the
circles which is classified either to the first class of triangles or to the second class of squares. If K=5 (dashed line
circle) it is assigned to the second class because there are 3 squares and 2 triangles inside that circle. If K=3 (solid
line circle) it is assigned to the second class because here 2 squares and 1 triangle inside that circle. It can be useful
if the weight contributions of the neighbours are considered because the nearer neighbours contribute more than the
distant ones. For example, in a common weighting scheme, individual neighbour is assigned to a weight of 1/d if
d is the distance to the neighbour. The shortest distance between any two neighbours is always a straight line and the
distance is known as Euclidean distance [7]. The limitation of the K-NN algorithm is it’s sensitive to the local
configuration of the data. The process of transforming the input data to a set of features is known as Feature
extraction. In Feature space, extraction is taken place on raw data before applying K-NN algorithm. The below
narrates the steps involved in a K-NN algorithm.
```sh
Start
↓
Initialization, define the parameter
↓
Calculate the distance between the test sample and all the training samples.
↓
Sort the Distance
↓
Take K-nearest neighbour
↓
Gather the category of nearest neighbour
↓
Apply simple majority of category
↓
End
```

# To Run MATLab Logistic Regression
![](matlab_değerleri_Lojistik_Regresyon.png)


### Run
```sh
$ run breast_cancer.m
```

# To Run Artificial Iintelligence
## It is an artificial intelligence study that gives results with %98 accuracy in the detection of breast cancer with the help of the KNN algorithm. The project was completed in October 2020. You may get errors on the code due to updates to the libraries in the future. It will be enough to change the library paths.
#### 4 --> Malignant (Kötü Huylu Kanser Hücresi)
#### 2 --> Benign (İyi Huylu Kanser Hücresi)
![](cancer-test2.png)

### Run
 ```sh
$ python cancer-test.py
```

## In this project, UCI Machine Learning Repository  data were used to train artificial intelligence.
![](logo-UCI.gif)
- UCI for breast cancer : [https://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+(original)]
