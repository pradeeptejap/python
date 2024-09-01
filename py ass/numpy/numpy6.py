import numpy as np

siz = int(input("Enter the number of random numbers: "))

arr = np.random.randint(50, 101, size=siz)

print("Array of random numbers:", arr)
