# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv(path)
print(df.head())
X = df.drop(labels='list_price', axis=1)
y = df['list_price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=6)



# --------------
import matplotlib.pyplot as plt

# code starts here        
cols = X_train.columns

plt.rcParams['figure.figsize'] = (12,12)
fig, axes = plt.subplots(nrows=3, ncols=3)
fig.suptitle('Lego Dataset', fontdict={'fontsize':14, 'fontweight':'bold'})
fig.subplots_adjust(top=0.8)
for i in range(0, 3):
    for j in range(0, 3):
        col = cols[i * 3 + j]
        axes[i, j].scatter(X_train[col], y_train)
        axes[i, j].set_title(f'{col}', fontdict={'fontsize':10, 'fontweight':'semibold'})
plt.tight_layout()
plt.show()


# code ends here



# --------------
# Code starts here
corr = X_train.corr(method='spearman')
print(corr)

X_train.drop(labels=['play_star_rating', 'val_star_rating'], axis=1, inplace=True)
X_test.drop(labels=['play_star_rating', 'val_star_rating'], axis=1, inplace=True)
# Code ends here


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Code starts here
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('Mean Squarred Error: %.3f' % mse)
print('R2_coefficient: %.3f' % r2)
# Code ends here


# --------------
# Code starts here

residual = y_test - y_pred
plt.hist(residual, edgecolor='w', ls='-.');
plt.show()
# Code ends here


