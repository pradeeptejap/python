l = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), (), ('d')]

for i in range(0,7):
    if len(l[i]) != 0 :
        print(l[i],end=" ")
    else:
        continue
