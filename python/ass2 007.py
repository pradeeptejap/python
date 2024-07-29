p1 = eval(input("Enter Age Of 1st Person: "))
p2 = eval(input("Enter Age Of 2nd Person: "))
p3 = eval(input("Enter Age Of 3rd Person: "))

if p1 < p2 :
    if p2 > p3:
        print("2nd Person is The Oldest")
    else :
        print("3rd person Is The Oldest")
elif p1 > p3 :
    print("1st person Is The Oldest:")
else :
    print("3rd Person Is The Oldest")