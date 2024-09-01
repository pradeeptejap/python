def big (a,b,c,d):
    if a > b :
        if a > c:
            if a > d:
                print(f"{a} is biggest")
            else :
                print(f"{d} is biggest")
        elif c > d :
            print(f"{c} is biggest")
        else :
            print(f"{d} is biggest")
    elif b > c :
        if b > d:
            print(f"{b} is biggest")
        else :
            print(f"{d} is biggest")
    elif c > d:
        print(f"{c} is biggest")
    else :
        print(f"{d} is biggest")

a = 1 
b = 5
c = 2
d = 7

big(a,b,c,d)
    