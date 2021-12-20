import numpy as np
import array

print(np.__version__)
L = list(range(10))
A = array.array("i", L)
print(A)
print(np.array(L))
print(np.array([1, 2, 3, 4], dtype="float32"))
print(np.array([range(i, i + 3) for i in [2, 4, 6]]))