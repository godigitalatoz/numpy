import numpy as np

def myadd(x, y):
    return x+y

myadd = np.frompyfunc(myadd, 2, 1)

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]

z = myadd(x, y)
print(z)

print(type(myadd))
