from scipy import stats
import pandas as pd

data = pd.read_csv('stroopdata.csv')
congruent = data['Congruent']
incongruent = data['Incongruent']


t_value, p_value = stats.ttest_rel(congruent, incongruent)
print(stats.ttest_rel(congruent, incongruent))

print('The t_value for this experiment is {}'.format(t_value))
print('The p_value for this experiment is {}'.format(p_value))