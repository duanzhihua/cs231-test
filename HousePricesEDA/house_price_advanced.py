# coding: utf-8
import numpy as np
import pandas as pd

train_df = pd.read_csv('./input/train.csv', index_col=0)
test_df = pd.read_csv('./input/test.csv', index_col=0)

train_df.head()

#get_ipython().run_line_magic('matplotlib', 'inline')
prices = pd.DataFrame({"price":train_df["SalePrice"], "log(price + 1)":np.log1p(train_df["SalePrice"])})
prices.hist()

y_train = np.log1p(train_df.pop('SalePrice'))

all_df = pd.concat((train_df, test_df), axis=0)

all_df.shape

y_train.head()


all_df['MSSubClass'].dtypes


all_df['MSSubClass'] = all_df['MSSubClass'].astype(str)


all_df['MSSubClass'].value_counts()


pd.get_dummies(all_df['MSSubClass'], prefix='MSSubClass').head()

all_dummy_df = pd.get_dummies(all_df)
all_dummy_df.head()

all_dummy_df.isnull().sum().sort_values(ascending=False).head(10)


mean_cols = all_dummy_df.mean()
mean_cols.head(10)


all_dummy_df = all_dummy_df.fillna(mean_cols)



all_dummy_df.isnull().sum().sum()



numeric_cols = all_df.columns[all_df.dtypes != 'object']
numeric_cols

numeric_col_means = all_dummy_df.loc[:, numeric_cols].mean()
numeric_col_std = all_dummy_df.loc[:, numeric_cols].std()
all_dummy_df.loc[:, numeric_cols] = (all_dummy_df.loc[:, numeric_cols] - numeric_col_means) / numeric_col_std


dummy_train_df = all_dummy_df.loc[train_df.index]
dummy_test_df = all_dummy_df.loc[test_df.index]


dummy_train_df.shape, dummy_test_df.shape



X_train = dummy_train_df.values
X_test = dummy_test_df.values




from sklearn.linear_model import Ridge
ridge = Ridge(15)




from sklearn.ensemble import BaggingRegressor
from sklearn.model_selection import cross_val_score



params = [1, 10, 15, 20, 25, 30, 40]
test_scores = []
for param in params:
    clf = BaggingRegressor(n_estimators=param, base_estimator=ridge)
    test_score = np.sqrt(-cross_val_score(clf, X_train, y_train, cv=10, scoring='neg_mean_squared_error'))
    test_scores.append(np.mean(test_score))


import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(params, test_scores)
plt.title("n_estimator vs CV Error");


params = [10, 15, 20, 25, 30, 40, 50, 60, 70, 100]
test_scores = []
for param in params:
    clf = BaggingRegressor(n_estimators=param)
    test_score = np.sqrt(-cross_val_score(clf, X_train, y_train, cv=10, scoring='neg_mean_squared_error'))
    test_scores.append(np.mean(test_score))



import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(params, test_scores)
plt.title("n_estimator vs CV Error");


from sklearn.ensemble import AdaBoostRegressor


params = [10, 15, 20, 25, 30, 35, 40, 45, 50]
test_scores = []
for param in params:
    clf = BaggingRegressor(n_estimators=param, base_estimator=ridge)
    test_score = np.sqrt(-cross_val_score(clf, X_train, y_train, cv=10, scoring='neg_mean_squared_error'))
    test_scores.append(np.mean(test_score))


plt.plot(params, test_scores)
plt.title("n_estimator vs CV Error");



params = [10, 15, 20, 25, 30, 35, 40, 45, 50]
test_scores = []
for param in params:
    clf = BaggingRegressor(n_estimators=param)
    test_score = np.sqrt(-cross_val_score(clf, X_train, y_train, cv=10, scoring='neg_mean_squared_error'))
    test_scores.append(np.mean(test_score))


plt.plot(params, test_scores)
plt.title("n_estimator vs CV Error");


from xgboost import XGBRegressor

params = [1,2,3,4,5,6]
test_scores = []
for param in params:
    clf = XGBRegressor(max_depth=param)
    test_score = np.sqrt(-cross_val_score(clf, X_train, y_train, cv=10, scoring='neg_mean_squared_error'))
    test_scores.append(np.mean(test_score))


import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(params, test_scores)
plt.title("max_depth vs CV Error"); 