import numpy as np
arr = np.random.randint(1, 101, size=10)

print("Original Array:", arr)

for i in range(0,10):
    if arr[i]%2 == 0:
        arr[i] = 0

print("Array after replacing even numbers with 0:", arr)
