from numpy import *

tup = tuple(random.randint(1,10,10))
for i in range(0,10):
    print("Random Numbers:", tup[i])

element_to_check = tup[0]
count = tup.count(element_to_check)

print(f"The element {element_to_check} appears {count} times.")
