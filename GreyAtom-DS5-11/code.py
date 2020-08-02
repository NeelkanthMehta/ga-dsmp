# --------------
# import the libraries
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

# Code starts here
df = pd.read_csv(path)
print(df.iloc[:5,:5])
X = df.drop(labels='insuranceclaim', axis=1)
y = df['insuranceclaim']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=6)
# Code ends here


# --------------
import matplotlib.pyplot as plt


# Code starts here
X_train['bmi'].plot.box();

q_value = X_train['bmi'].quantile(q=.95)

print(y_train.value_counts())
# Code ends here


# --------------
# Code starts here
import seaborn as sns

relation = X_train.corr()
print(relation)

sns.pairplot(X_train, kind='reg', diag_kind='kde');
plt.show()
# Code ends here


# --------------
import seaborn as sns
import matplotlib.pyplot as plt

# Code starts here
cols = ['children','sex','region','smoker']

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20,20))
for i in range(0,2):
    for j in range(0, 2):
        col = cols[i*2 + j]
        sns.countplot(x=X_train[col], hue=y_train, ax=axes[i,j])
plt.tight_layout()
plt.show()
# Code ends here


# --------------
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# parameters for grid search
parameters = {'C':[0.1,0.5,1,5]}

# Code starts here
lr = LogisticRegression(random_state=9)
grid = GridSearchCV(estimator=lr, param_grid=parameters)
grid.fit(X_train, y_train)
y_pred = grid.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
# Code ends here


# --------------
from sklearn.metrics import roc_auc_score
from sklearn import metrics

# Code starts here
score = roc_auc_score(y_test, y_pred)
y_pred_proba = grid.predict_proba(X_test)[:,1]
fpr, tpr, _ = metrics.roc_curve(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)

plt.plot(fpr,tpr,label="Logistic model, auc="+str(roc_auc))
plt.show()
# Code ends here

