import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from pandas.core.common import random_state
from sklearn.linear_model import LinearRegression

from google.colab import files
uploaded = files.upload()

df_sal = pd.read_csv('Morning_Routine_Productivity_Dataset.csv')
df_sal.head()

# @title Sleep Duration (hrs) vs Productivity Score (1-10)

from matplotlib import pyplot as plt
df_sal.plot(kind='scatter', x='Sleep Duration (hrs)', y='Productivity Score (1-10)', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

df_sal.info()

df_sal.describe()

plt.scatter(df_sal['Sleep Duration (hrs)'], df_sal['Productivity Score (1-10)'], color = 'lightcoral')
plt.title('Productivity Score (1-10) vs Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Productivity Score (1-10)')
plt.box(False)
plt.show()

X = df_sal.iloc[:, :1]  # independent
y = df_sal.iloc[:, 1:]  # dependent

X = df_sal['Sleep Duration (hrs)']
y = df_sal['Productivity Score (1-10)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

# Drop rows with NaN values in y_train and corresponding rows in X_train
not_nan_mask = y_train.notna()
X_train = X_train[not_nan_mask]
y_train = y_train[not_nan_mask]

regressor = LinearRegression()
regressor.fit(X_train.values.reshape(-1, 1), y_train)

y_pred_test = regressor.predict(X.values.reshape(-1, 1))     # predicted value of y_test
y_pred_train = regressor.predict(X_train.values.reshape(-1, 1))   # predicted value of y_train

plt.scatter(X_train, y_train, color = 'lightcoral')
plt.plot(X_train, y_pred_train, color = 'firebrick')
plt.title('Productivity Score (1-10) vs Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Productivity Score (1-10)')
plt.legend(['X_train/Pred(y_test)', 'X_train/y_train'], title = 'Sal/Exp', loc='best', facecolor='white')
plt.box(False)
plt.show()

X = pd.get_dummies(df_sal['Sleep Duration (hrs)'])
y = df_sal['Productivity Score (1-10)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Drop rows with NaN values in y_train and corresponding rows in X_train
not_nan_mask = y_train.notna()
X_train = X_train[not_nan_mask]
y_train = y_train[not_nan_mask]


regressor = LinearRegression()
regressor.fit(X_train, y_train)

print(regressor.predict([[0]])
)