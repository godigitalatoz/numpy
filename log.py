from math import log
import numpy as np

nplog = np.frompyfunc(log, 2, 1)

arr1 = [1000, 100, 10]
arr2 = [10, 5, 2]

arr3 = nplog(arr1, arr2)


print(arr3)



