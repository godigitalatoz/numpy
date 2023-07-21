from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6,], size=(1000))
sns.distplot(x, hist=False)

plt.show()