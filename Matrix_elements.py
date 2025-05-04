import numpy as np
import time

start = time.perf_counter()
neighbors = [(1, 2), (3, 4), (5, 6)]
far = [(2,3), (3,3), (1,1), (1,2)]
total = neighbors+far
H101 = np.zeros((6,6),dtype=int)  # let's say for a 6x6 lattice
print(total)
for pairs in total:
    i = pairs[0]
    j=pairs[1]
    H101[i-1,j-1]=1

print(np.shape(H101))
print((H101))

end = time.perf_counter()

print(f"Took {end - start:.6f} seconds")
