from array import *

arr = [1,2,3,4,5,1,6,3]

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            print(arr[j])