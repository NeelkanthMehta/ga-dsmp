# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)

#Code starts here 
data['Gender'].replace(to_replace='-', value='Agender', inplace=True)

gender_count = data['Gender'].value_counts()
print(gender_count)



# --------------
#Code starts here
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

alignment = data['Alignment'].value_counts()

plt.pie(alignment, labels=alignment.index.tolist())
plt.title('Character Alignment', fontweight='semibold')
plt.show()


# --------------
#Code starts here

#Subsetting the data with columns ['Strength', 'Combat']
sc_df = data[['Strength','Combat']].copy()

#Finding covariance between 'Strength' and 'Combat'
sc_covariance = sc_df.cov().iloc[0,1]

#Finding the standard deviation of 'Strength'
sc_strength = sc_df['Strength'].std()

#Finding the standard deviation of 'Combat'
sc_combat = sc_df['Combat'].std()

#Calculating the Pearson's correlation between 'Strength' and 'Combat'
sc_pearson = sc_covariance/(sc_combat*sc_strength)

print("Pearson's Correlation Coefficient between Strength and Combat : ", sc_pearson)


#Subsetting the data with columns ['Intelligence', 'Combat']
ic_df = data[['Intelligence','Combat']].copy()

#Finding covariance between 'Intelligence' and 'Combat'
ic_covariance = ic_df.cov().iloc[0,1]

#Finding the standard deviation of 'Intelligence'
ic_intelligence = ic_df['Intelligence'].std()

#Finding the standard deviation of 'Combat'
ic_combat = ic_df['Combat'].std()

#Calculating the Pearson's correlation between 'Intelligence' and 'Combat'
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)

print("Pearson's Correlation Coefficient between Intelligence and Combat : ", ic_pearson)

#Code ends here


# --------------
#Code starts here
total_high = data['Total'].quantile(q=0.99)

super_best = data[data['Total'] > total_high]

super_best_names = super_best['Name'].tolist()


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows=1, ncols=3, sharey=True)

ax_1.boxplot(data['Intelligence'])
ax_1.set_title('Intelligence')
ax_2.boxplot(data['Speed'])
ax_2.set_title('Speed')
ax_3.boxplot(data['Power'])
ax_3.set_title('Power')

plt.tight_layout()
plt.show()


