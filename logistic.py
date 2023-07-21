from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 

x = random.logistic(loc=1, scale=2, size=(1000))
sns.distplot(x, hist=False)


plt.show()