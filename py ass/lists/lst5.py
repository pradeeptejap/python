count = int(input("Enter No Of Elements In A List: "))

print()

ele = []

for i in range(count):
    els = input(f"Enter {i+1} Element: ")
    ele.append(els)

print()

le = len(ele)

if (le == 0):
    print("list is empty")
elif (le != 0):
    print(ele)