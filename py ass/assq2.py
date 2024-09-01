from array import *
arr = array('i',)
size = int(input("Enter How Many Elements In Array: "))

for i in range(size):
    ele = int(input(f"Enter {i+1} element: "))
    arr.append(ele)

print()

print(arr)

print()

print("updation")
arr[2] = 20

print(arr)

arr.pop(size-1)

print()

print("deletion: ")
print(arr)

print()

ser = int(input("Enter Element To Search: "))

if ser in arr:
    print("Element Found At" ,arr.index(ser))
else :
    print("Element Not Found")

