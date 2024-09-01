import random

rows, cols = 3, 4
array_2d = [[random.randint(1, 20) for i in range(cols)] for j in range(rows)]

print("2D Array (3x4):")
for row in array_2d:
    print(row)
