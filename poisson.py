import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

x = np.random.poisson(lam=1, size=1000)

sns.distplot(x, kde=False)

plt.show()