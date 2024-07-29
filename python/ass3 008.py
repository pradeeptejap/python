no = 1

while (no <= 1000) :
    nos = str(no)
    let = len(nos)
    sum = 0

    for i in nos:
        sum += int(i) ** let 
    
    if sum == no :
        print(no, end=" - ")
    no+=1