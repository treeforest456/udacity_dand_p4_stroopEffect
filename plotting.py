


# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Importing
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('stroopdata.csv')

plt.title('Histogram plot')
plt.hist(data['Congruent'], label='congruent')
plt.xlabel('Time')
plt.legend()
plt.show()

plt.title('Histogram plot')
plt.hist(data['Incongruent'], label='incongruent')
plt.xlabel('Time')
plt.legend()
plt.show()


plt.title('Scatter plot')
plt.scatter(x=range(data.shape[0]), y = data.iloc[:, 0], label = 'congruent')
plt.scatter(x=range(data.shape[0]), y = data.iloc[:, 1], label = 'incongruent')
plt.legend()
plt.show()


plt.style.use('ggplot')
plt.boxplot([data.iloc[:, 0], data.iloc[:, 1]])
plt.grid(linestyle='-', linewidth=2)
plt.title('Boxplot')
plt.xticks([1, 2], ['congruent', 'incongruent'])
plt.show()