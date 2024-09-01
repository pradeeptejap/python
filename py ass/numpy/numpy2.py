from numpy import *

num = 100
arr = [random.randint(1,100,10)]
print(arr)

for i in range(num):
    if i % 10 == 0:
        print(i)