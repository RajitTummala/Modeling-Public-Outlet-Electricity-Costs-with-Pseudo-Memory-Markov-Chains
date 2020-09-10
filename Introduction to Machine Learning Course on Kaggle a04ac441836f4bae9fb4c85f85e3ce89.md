# Introduction to Machine Learning Course on Kaggle

Created Time: Aug 14, 2020 10:58 AM
Deadline: Aug 14, 2020
Done: No
Goal: https://www.notion.so/Become-a-Published-Researcher-530f1f72449540f5b97bcb0b02174a38
Ideas: https://www.notion.so/Kaggle-Python-ML-Course-Notes-e3904a3db654462d8ea75bbc40f7da76
Motifs: https://www.notion.so/notes-ccaf130aaece46df84de2e937c35f590, https://www.notion.so/cs-351676da17ba4751a6cbc5e6e9e00fa5
Progress: Completed
Tags: #1

# Selecting Data for Modeling

```python
import pandas as pd

data = pd.read_csv(file_path)
data.columns

>>> Index(['Column 1','Column 2','Column 3'])

if missing data values
data = data.dropna(axis=0)
```

### Dot Notation for Prediction Target

You are able to take out a variable from a DataFrame through ***dot-notation.*** Single column stored in a ***series***, a DataFrame with single column of data.

By convention ***prediction target*** is called assigned the variable **y**:

```python
y = data.AvgSleepingTimeForButter
```

### Choosing "Features"

Columns that are inputted into are model are called ***features**.* We create an array with all the desired columns as strings and then assign it to variable **x:**

```python
key_features = ['Sleeping Frequency','Sleeping Duration','Sleep Quality']
x = data[key_features]
```

### describe() and head()

`describe()` - gives key statistical features like mean, count, sd, etc.

`head()` - gives first five data rows

# Building the Model

Using scikit-learn to build models, library written as ***sklearn***

### Steps to Building a Model

1. *Define Model:* What type of model is it going to be? Neural Network? Decision Tree?
2. *Fit*: Captures the patterns in the data
3. *Predict*
4. *Evaluate*

```python
from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor(random_state=1)

model.fit(x,y)

#training dataset = x

## Specifying a number for the random_state ensures you get the same results

#prediction dataset = futurex

model.predict(futurex)
```

# Model Validation

### What is Model Validation

DON'T measure predicted with values on the same dataset trained, you want to see if the patterns your  model found extend beyond the training dataset.

### Predictive Accuracy Metric

One measure of predictive accuracy is ***Mean Absolute Error*.**

```python
from sklearn.metrics from mean_absolute_error
predicted_AvgSleepingTimeForButter = model.predict(futurex)

#y = actual_AvgSleepingTimeForButter
mean_absolute_error(predicted_AvgSleepingTimeForButter, y)
```

### Splitting the Dataset

```python
from sklearn.model_selection from train_test_split

train_X, train_Y, val_X, val_Y = train_test_split(X, y, random_state = 0)

#Create Model

model = DecisionTreeRegressor(random_state = 0)
model.fit(train_X, train_Y)

predicted_val_Y = model.predict(val_X)

mean_absolute_error(predicted_val_Y, val_Y)
```

### Experimenting with Different Models (Underfitting vs. Overfitting)

![Introduction%20to%20Machine%20Learning%20Course%20on%20Kaggle%20a04ac441836f4bae9fb4c85f85e3ce89/OverUnderFitting.png](Introduction%20to%20Machine%20Learning%20Course%20on%20Kaggle%20a04ac441836f4bae9fb4c85f85e3ce89/OverUnderFitting.png)

- Full Code (WARNING: DIFFICULT TO READ)

    ```python
    def minimize(candidate_max_leaf_nodes):
        get_MAE_values = {get_mae(candidate_max_leaf_nodes[i],train_X,val_X,train_y, val_y):candidate_max_leaf_nodes[i] for i in range(len(candidate_max_leaf_nodes))}
        best_tree_size = get_MAE_values[min(get_MAE_values.keys())]
        return best_tree_size

    def minimizeMAE(candidate_max_leaf_nodes):
        get_MAE_values = {get_mae(candidate_max_leaf_nodes[i],train_X,val_X,train_y, val_y):candidate_max_leaf_nodes[i] for i in range(len(candidate_max_leaf_nodes))}
        a = min(get_MAE_values.keys())
        return a
    def minimize_data(candidate_max_leaf_nodes):
        get_MAE_values = {candidate_max_leaf_nodes[i]:get_mae(candidate_max_leaf_nodes[i],train_X,val_X,train_y, val_y) for i in range(len(candidate_max_leaf_nodes))}
        array = []
        array = [item2 for item2 in get_MAE_values.values()]
        #[item for item in get_MAE_values.values()]
        return array
    experiment = []
    for i in range(200):
        experiment.append(i+2)

    import matplotlib.pyplot as plt

    minMaxLeafNode = minimize(experiment)
    minMAE = minimizeMAE(experiment)

    b = 0
    b = minMaxLeafNode+2000
    c = 0
    c = int(minMAE-20)

    plt.figure(figsize=(20,10))
    plt.plot(experiment, minimize_data(experiment))
    plt.plot(minMaxLeafNode, minMAE, 'yo')
    plt.axis([0,200, 0,45000])
    plt.text(10,40000,r'Underfitting')
    plt.text(150,35000,r'Overfitting')
    a = 'Ideal Point: (Max Leaf Nodes = {}),(MAE = {:.10})'.format(minMaxLeafNode,minMAE)
    plt.text(minMaxLeafNode,minMAE+2000,a)
    plt.ylabel(r'MAE (in dollars)')
    plt.xlabel('Max Leaf Nodes in Decision tree')

    plt.show()
    ```

# Random Forests

Even today's most sophisticated machine learning techniques suffer from overfitting and underfitting, but many models have clever ideas which lead to better performance. 

In real life, trees make up forests.

In coding world, decision trees make up random forests. Essentially, random forests predict the averaged value from all of its decision trees.

```python
from sklearn.ensemble import RandomForestRegressor
from sylearn.metrics import mean_absolute_error

forest_model = RandomForestRegressor(random_state = 1)
forest_model.fit(train_X,train_y)

model_prediction = forest_model.predict(val_X)

mean_absolute_error(model_prediction,val_y)
```

# Replacing Missing Values

### Option 1: Dropping All Values Across a Column

May lose potentially value from a column only because a few rows lack data.

![https://i.imgur.com/Sax80za.png](https://i.imgur.com/Sax80za.png)

```python
#checking to see if there are any NaN values in any of the columns
columns_with_missing = [col for col in X_train.columns if X_train[col].isnull().any()]

X_train_opt_1 = X_train.drop(columns_with_missing, axis = 1)
X_valid_opt_2 = X_valid.drop(columns_with_missing, axis = 1)

#user-defined function
score_dataset(X_train_opt_1, X_valid_opt_2, y_train, y_valid)
```

### Option 2: Imputation

Placing values in the NaN based on the central tendencies of the column with the missing data.

![https://i.imgur.com/4BpnlPA.png](https://i.imgur.com/4BpnlPA.png)

```python
from sklearn.impute import SimpleImputer

my_inputer = SimpleInputer()

#inputting the data
X_train_opt_2 = pd.DataFrame(my_inputer.fit_transform(X_train))
X_valid_opt_2 = pd.DataFrame(my_inputer.transform(X_valid))

#inputting loses the columns, so place them back
X_train_opt_2.columns = X_train.columns
X_valid_opt_2.columns = X_valid.columns

#user-defined functions
score_dataset(X_train_opt_2, X_valid_opt_2, y_train, y_valid)
```

### Option 3: Remembered Imputation

Creates another column for each column with imputed values to state which values in that column were imputed and which ones are not.

![https://i.imgur.com/UWOyg4a.png](https://i.imgur.com/UWOyg4a.png)

```python
from sklearn.impute import SimpleImputer

X_train_rem = X_train.copy()
X_valid_rem = X_valid.copy()

my_imputer = SimpleImputer()

for col in columns_with_missing:
	X_train_rem[col + '_was_missing'] = X_train[col].isnull()
	x_valid_rem[col + '_was_missing'] = X_valid[col].isnull()

X_train_rem = pd.DataFrame(my_imputer.fit_transform(X_train_rem))
X_valid_rem = pd.DataFrame(my_imputer.transform(X_valid_rem))

X_train_rem.columns = X_train.columns
X_valid_rem.columns = X_valid.columns

score_dataset(X_train_rem, X_valid_rem, y_train, y_valid)
```

# Appendix A

## I. Models

### `Decision Tree`

Identifies key features to separate and group data, and then predicts future data based on these ***leafs*.**

```python
from sklearn.tree import DecisionTreeRegressor
decision_tree = DecisionTreeRegressor(max_leaf_nodes=10)

----
#max_leaf_nodes determines maximum number of leaves at end of decision tree (NOTE: cannot be 1 or None)
```

### `Random Forest`

In real life, trees make up forests. 

In coding world, decision trees make up random forests. Essentially, random forests predict the averaged value from all of its decision trees.

```python
from sklearn.ensemble import RandomForestRegressor
forest_model = RandomForestRegressor()
```

## II. Data Processing

### `DataFrame.isnull().sum()`

Returns an array on ints with the number of missing values in each column across the dataset

```python
missing_vals_per_column = X_train.isnull().sum()

#Prints only columns with actual missing values (excludes the zeros)
print(missing_vals_per_column > 0)
```

### `DataFrame.shape()`

Gives shape of dataset i.e. how many rows x columns

```python
X_train.shapes()
>>> (3324,10)

#Means 3324 rows and 10 columns
```

### `DataFrame.select_dtypes()`

Select what types of data you would like

```python
# excludes any string / categorical variables with ['object']
X = X_full.select_dtypes(exclude = ['object'])
X_test = X_test.select_dtypes(exlcude = ['object'])
```

### `DataFrame.dropna()`

Removes rows without target values 

```python
import pandas as pd

#Axis = 0 says focus on on dropping rows (compare with axis = 1, which drops columns)
#Subset says drop rows with NaN in this column or columns
#InPlace says do you want to return a value or not, if this is True, I will perform change on data without returning anything

X_full.dropna(axis = 0, subset = ['SalePrice'], inplace = True)
```

### `DataFrame.drop()`

Removes specified rows

```python
import pandas as pd

#Ideally before DataFrame.drop() you would do this:
y = X_full.SalePrice

#['SalePrice'] is specified column, axis = 1 means remove column(s), inplace will return nothing
X_full.drop(['SalePrice'], axis = 1, inplace = True)
```

### `SimpleImputer()`

Inputs educated guesses for the NaN in the data

```python
import pandas as pd
from sklearn.impute import SimpleImputer()
my_imputer = SimpleImputer()

#fits the imputer based on X_train and imputes values to imputed_X_train
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid)

#remember to add back the columns
imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns
```

### `train_test_split(X, y, random_state = 0)`

Creates a training and validation data set from the whole dataset. Make sure `random_state = 0` because that controls how the data is split.

```python
from sklearn.model_selection import train_test_split

X = keyFeaturesArray
y = predictionArray

train_X, train_y, val_X, val_y = train_test_split(X, y, random_state = 0)
```

## III. Predictive Accuracy Methods

### `Mean Absolute Error`

Checks how far from the actual value the model's predicted value is.

```python
from skylearn.metrics import mean_absolute_error

mean_absolute_error(pred_val, val_y)
```