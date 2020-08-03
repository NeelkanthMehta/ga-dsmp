# --------------
import pandas as pd
from sklearn.model_selection import train_test_split
#path - Path of file 

# Code starts here
df = pd.read_csv(path)
X = df.drop(labels=['customerID','Churn'], axis=1)
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=0)


# --------------
import numpy as np
from sklearn.preprocessing import LabelEncoder


# Code starts here
X_train['TotalCharges'].replace(' ',np.NaN, inplace=True)
X_test['TotalCharges'].replace(' ',np.NaN, inplace=True)

X_train['TotalCharges'] = X_train['TotalCharges'].astype(np.float64)
X_test['TotalCharges'] = X_test['TotalCharges'].astype(np.float64)

X_train['TotalCharges'].fillna(X_train['TotalCharges'].mean(), inplace=True)
X_test['TotalCharges'].fillna(X_train['TotalCharges'].mean(), inplace=True)

print(X_train.isnull().sum())
print('')
print(X_test.isnull().sum())

categorical_cols = X_train.select_dtypes(include='O').columns.tolist()

for i in categorical_cols:
    le = LabelEncoder()
    X_train[i] = le.fit_transform(X_train[i])
    X_test[i] = le.transform(X_test[i])

y_train.replace({'Yes':1, 'No':0}, inplace=True)
y_test.replace({'Yes':1, 'No':0}, inplace=True)



# --------------
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

# Code starts here
print(pd.concat([X_train, y_train], axis=1).sample(5))
print('')
print(pd.concat([X_test, y_test], axis=1).sample(5))

ada_model1 = AdaBoostClassifier(random_state=0)
ada_model1.fit(X_train, y_train)
y_pred = ada_model1.predict(X_test)
ada_score = accuracy_score(y_test, y_pred)
ada_cm = confusion_matrix(y_test, y_pred)
ada_cr = classification_report(y_test, y_pred)



# --------------
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV

#Parameter list
parameters={'learning_rate':[0.1,0.15,0.2,0.25,0.3],
            'max_depth':range(1,3)}

# Code starts here
xgb_model = XGBClassifier(random_state=0)
xgb_model.fit(X_train, y_train)
y_pred = xgb_model.predict(X_test)
xgb_score = accuracy_score(y_test, y_pred)
xgb_cm = confusion_matrix(y_test, y_pred)
xgb_cr = classification_report(y_test, y_pred)

clf_model = GridSearchCV(estimator=xgb_model, param_grid=parameters)
clf_model.fit(X_train, y_train)
y_pred = clf_model.predict(X_test)
clf_score = accuracy_score(y_test, y_pred)
clf_cm = confusion_matrix(y_test, y_pred)
clf_cr = classification_report(y_test, y_pred)

print('XGB: %.3f vs CLF: %.3f' %(xgb_score, clf_score))
print('XGB CM:\n', xgb_cm)
print('CLF CM:\n', clf_cm)
print('')
print('XGB CR:\n', xgb_cr)
print('CLF CR:\n', clf_cr)



