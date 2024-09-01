i = int(input("no Of Subjects: "))

print()

subm = []

for i in range(i):
    m = int(input(f"Enter {i+1} Sub marks: "))
    subm.append(m)

mn = subm[0]
mx = subm[0]

for m in subm:
    if mn > m:
        mn = m
    if mx < m:
        mx = m

print()

print(f"minimum VAlue is {mn}")

print()
print(f"maximum value is {mx}")