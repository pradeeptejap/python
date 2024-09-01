marks = []

for i in range(1,6):
    m=float(input(f"Enter {i} subject marks: "))
    marks.append(m)

ord =sorted(marks)
tot = sum(marks)
mn = min(marks)
mx = max(marks)

print()

print(f"Your Marks Are: {ord}")
print(f"The Total Marks Is : {tot}")
print(f"Your Minimum Marks Are : {mn}")
print(f"Your Maxmimuum Marks Are: {mx}")