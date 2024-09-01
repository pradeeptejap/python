from array import *

arr = array('i',)

size = int(input("Enter No Of Elements In Array: "))
for i in range(size):
    ele=int(input(f"Enter {i+1} Element: "))
    arr.append(ele)
mid = size // 2

print("first half: ",arr[:mid])
print("second half: ",arr[mid:])