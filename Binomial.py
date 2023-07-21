import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

x = np.random.binomial(n=10, p=0.5, size=1000)
 
sns.distplot(x, hist=True, kde=False)

plt.show()