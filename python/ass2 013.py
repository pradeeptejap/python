n1 = input("enter 1st person name: ")
p1 = eval(input("enter 1st person age: "))
n2 = input("enter 2nd person name: ")
p2 = eval(input("enter 2nd person age: "))

if p1 > p2 :
    print(f"{n1} is older than {n2}")
elif p2 > p1 :
    print(f"{n2} is older than {n2}")
else :
    print(f"{n1} and {n2} are at same age")