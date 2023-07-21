import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

x = np.random.normal(loc=5, scale=2, size=(100))
sns.distplot(x, hist=False)

plt.show()