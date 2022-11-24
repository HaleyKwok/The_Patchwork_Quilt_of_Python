# The_Python_Challenge

## Day 1 Data Preprocessing

Dataset:
``` python
	Country	Age	Salary	Purchased
0	France	44.0	72000.0	No
1	Spain	27.0	48000.0	Yes
2	Germany	30.0	54000.0	No
3	Spain	38.0	61000.0	No
4	Germany	40.0	NaN	Yes
5	France	35.0	58000.0	Yes
6	Spain	NaN	52000.0	No
7	France	48.0	79000.0	Yes
8	Germany	50.0	83000.0	No
9	France	37.0	67000.0	Yes
```
X is the matrix of features, y is the dependent variable vector

``` python
X = dataset.iloc[:, :-1].values # we need the array, not the dataframe
y = dataset.iloc[:, 3].values # we need 1010100 to label that
```



To make an dataframe to an array, we need
1. Imputer to make it as mean for the null values
``` python
# from sklearn.preprocessing import Imputer
from sklearn.impute import SimpleImputer as Imputer
# old version: class sklearn.preprocessing.Imputer(missing_values=’NaN’, strategy=’mean’, axis=0, verbose=0, copy=True)  https://blog.csdn.net/weixin_43582443/article/details/111145027

imputer = Imputer(missing_values=np.nan,strategy="mean")
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
X

# return
array([['France', 44.0, 72000.0],
       ['Spain', 27.0, 48000.0],
       ['Germany', 30.0, 54000.0],
       ['Spain', 38.0, 61000.0],
       ['Germany', 40.0, 63777.77777777778],
       ['France', 35.0, 58000.0],
       ['Spain', 38.77777777777778, 52000.0],
       ['France', 48.0, 79000.0],
       ['Germany', 50.0, 83000.0],
       ['France', 37.0, 67000.0]], dtype=object)
```
2. Use LabelEncoder to make it as number [1][0]

``` python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[ : , 0] = labelencoder_X.fit_transform(X[ : , 0])

# onehotencoder = OneHotEncoder(categorical_features = [0])
onehotencoder = OneHotEncoder()
X = onehotencoder.fit_transform(X).toarray()

# return
array([[0., 1., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        1., 0., 1., 0., 0., 1., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        1., 0., 1., 0., 1., 0., 1., 0., 0., 1., 1., 0., 1., 0.],
       [1., 0., 1., 0., 0., 1., 0., 1., 1., 0., 1., 0., 1., 0., 1., 0.,
        1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 0., 1., 1., 0., 1., 0.,
        1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.],
       [1., 0., 0., 1., 1., 0., 1., 0., 0., 1., 1., 0., 1., 0., 1., 0.,
        1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 0., 1.,
        1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.],
       [1., 0., 1., 0., 0., 1., 1., 0., 1., 0., 1., 0., 1., 0., 0., 1.,
        1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        1., 0., 0., 1., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.],
       [1., 0., 0., 1., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        1., 0., 0., 1., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0., 1., 0.,
        1., 0., 1., 0., 0., 1., 1., 0., 1., 0., 1., 0., 1., 0
        ......])

labelencoder_Y = LabelEncoder()
Y =  labelencoder_Y.fit_transform(y)

# return
array(['No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes'])
```

---
## Day 2 Linear Regression
``` python
plt.scatter(X_test , Y_test, color = 'red')
plt.plot(X_test , regressor.predict(X_test), color ='blue')
```
---
## Day 3 Multiple Linear Regression

``` python
# Encoding Categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[: , 3] = labelencoder.fit_transform(X[ : , 3]) # turn the country into array of numbers
onehotencoder = OneHotEncoder()
X = onehotencoder.fit_transform(X).toarray()
```


**Avoiding the Dummy Variable Trap**
The Dummy Variable trap is a scenario in which two or more variables are nigniv correlated: in simple terms. 
One variable can be predicted trom the others. Intuitivelv. there is a duplicate category: if we dropped the male category it is inferently detined in the female category zero remale value The solution to the dummy variable trap is to drop one of the categorical variables - it there are m number of categories,  use m-1 in the model, the value left out can be thought of as the reference value.

``` python
X = X[: , 1:] 
```

---
## Day 4-6 Logistic Regression

**Sigmoid Function**
The Sigmoid Function is an S-shaped curve that can take any real-values number and map it into a value between the range of 0 and 1, but never exactly at those limits.

Dateset:
``` python
User ID	Gender	Age	EstimatedSalary	Purchased
0	15624510	Male	19	19000	0
1	15810944	Male	35	20000	0
2	15668575	Female	26	43000	0
3	15603246	Female	27	57000	0
4	15804002	Male	19	76000	0
...	...	...	...	...	...
395	15691863	Female	46	41000	1
396	15706071	Male	51	23000	1
397	15654296	Female	50	20000	1
398	15755018	Male	36	33000	0
399	15594041	Female	49	36000	1
```

``` python
X = dataset.iloc[:, [1, 2]].values
y = dataset.iloc[:, 4].values

# return
array([['Male', 19],
       ['Male', 35],
       ['Female', 26],
       ['Female', 27],
       ['Male', 19],
       ['Male', 27],
       ['Female', 27],
       ['Female', 32],
       ['Male', 25],
       ['Female', 35],
       ['Female', 26],
       ['Female', 26],
       ['Male', 20],
       ['Male', 32],
       ['Male', 18],
       ['Male', 29],
       ['Male', 47],
       ['Male', 45],
       ['Male', 46], 
       ......])
```

```python
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
X[ : , 0] = labelencoder_X.fit_transform(X[ : , 0])
X
# return
array([[1, 19],
       [1, 35],
       [0, 26],
       [0, 27],
       [1, 19],
       [1, 27],
       [0, 27],
       [0, 32],
       [1, 25],
       [0, 35],
       [0, 26],
       ......])
```


```python
new_data = pd.get_dummies(dataset.Gender)
merged = pd.concat([new_data, dataset], axis = 1)
new_data
```

Then, 
1. Splitting the dataset into the Training set and Test set
2. Logistic Regression
3. Predicting the Test set results
4. Confusion Matrix
5. Accuracy Score

---
<<<<<<< HEAD
## Day 15 SVM
Kernal
1. Linear
2. Rbf
3. Sigmoid
4. Polynomial

Gamma
1. Auto
2. Scale

Regularization
1. C

Margin
1. Soft
2. Hard









---
=======
>>>>>>> 1dc39c354e81ea783f682c229da4d9fd99780c8e
