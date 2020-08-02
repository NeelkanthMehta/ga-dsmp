# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(path)

data['Rating'].plot(kind='hist', edgecolor='w', ls='-.');
plt.title('Distribution of Ratings', fontweight='semibold')
plt.show()

data = data[data['Rating'] <= 5]

data['Rating'].plot(kind='hist', edgecolor='w', ls='-.');
plt.title('Distribution of Ratings', fontweight='semibold')
plt.show()



# --------------
# code starts here
total_null = data.isnull().sum()
percentage_null = total_null.div(data.isnull().count())
missing_data = pd.concat([total_null, percentage_null], axis=1, keys=['Total', 'Percent'])
print(missing_data)
print('')
data.dropna(inplace=True)
total_null_1 = data.isnull().sum()
percentage_null_1 = total_null_1.div(data.isnull().count())
missing_data_1 = pd.concat([total_null_1, percentage_null_1], axis=1, keys=['Total', 'Percent'])
print(missing_data_1)
# code ends here


# --------------

#Code starts here
import seaborn as sns

sns.catplot(x="Category",y="Rating",data=data, kind="box", height = 10)
plt.xticks(rotation=90)
plt.title('Rating vs Category [Boxplot]', fontweight='semibold')
plt.show()
#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
print(data['Installs'].value_counts())

data['Installs'] = data['Installs'].str.replace(',','')
data['Installs'] = data['Installs'].str.replace('+','').astype(np.int64)
print(data['Installs'].value_counts())
le = LabelEncoder()
data['Installs'] = le.fit_transform(data['Installs'])

sns.regplot(x="Installs", y="Rating", data=data);
plt.title('Rating vs Installs [RegPlot]', fontweight='semibold')
plt.show()
#Code ends here



# --------------
#Code starts here
print(data['Price'].value_counts(ascending=False))
data['Price'] = data['Price'].str.lstrip('$').astype(np.float)

sns.regplot(x="Price", y="Rating", data=data)
plt.title('Rating vs Price [RegPlot]', fontweight='semibold')
plt.show()

#Code ends here


# --------------

#Code starts here
data['Genres'].unique()
data['Genres'] = data['Genres'].str.split(';').str[0]
gr_mean = data[['Genres','Rating']].groupby('Genres', as_index=False).mean()
print(gr_mean.describe())
gr_mean = gr_mean.sort_values(by='Rating')
print(gr_mean.min()[0], gr_mean.max()[0])
#Code ends here


# --------------

#Code starts here
print(data['Last Updated'].sample(10))
data['Last Updated'] = pd.to_datetime(data['Last Updated'], yearfirst=True)
max_date = data['Last Updated'].max()
data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days

sns.regplot(x="Last Updated Days", y="Rating", data=data);
plt.title('Rating vs Last Updated [RegPlot]', fontweight='semibold')
plt.show()
#Code ends here


