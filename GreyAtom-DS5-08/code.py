# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

z_critical = stats.norm.ppf(0.95)
sample_size = 2000

# Load the dataset
data = pd.read_csv(path)

data_sample = data.sample(n=sample_size, random_state=0)

sample_mean = data_sample['installment'].mean()
sample_std = data_sample['installment'].std()

margin_of_error = round(z_critical * (sample_std/ np.sqrt(sample_size)),2)
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)

true_mean = data['installment'].mean()

print(confidence_interval[0] < true_mean and true_mean < confidence_interval[1])



# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size = np.array([20,50,100])

#Code starts here
fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True)
fig.set_size_inches(4,8)
for i in range(len(sample_size)):
    m = []
    for j in range(1000):
        m.append(data['installment'].sample(n=sample_size[i]).mean())
    mean_series = pd.Series(m)
    axes[i].hist(mean_series, bins=40, edgecolor='w', ls='-.')
    axes[i].grid()
plt.tight_layout()
plt.show()


# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here
data['int.rate'] = data['int.rate'].str.strip('%').astype(float).div(100)

z_statistic, p_value = ztest(x1=data.loc[data['purpose'] == 'small_business','int.rate'], value=data['int.rate'].mean(), alternative='larger')

inference = 'Reject' if p_value < 0.05 else 'Fail to Reject'
print(inference)



# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here
z_statistic, p_value = ztest(x1=data.loc[data['paid.back.loan']=='No','installment'], x2=
data.loc[data['paid.back.loan']=='Yes','installment'])

inference = 'Reject the Null' if p_value < 0.05 else 'Fail to Reject'
print(inference)



# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
yes = data.loc[data['paid.back.loan'] == 'Yes','purpose'].value_counts()
no = data.loc[data['paid.back.loan'] == 'No','purpose'].value_counts()

observed = pd.concat([yes.T, no.T], axis=1, keys=['Yes','No'])

chi2, p, dof, ex = chi2_contingency(observed)

inference = 'Reject the Null' if p < critical_value else 'Fail to Reject'
print(inference)



