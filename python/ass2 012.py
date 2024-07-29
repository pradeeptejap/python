no1 = eval(input("Enter A Number:"))
no2 = eval(input("Enter 2nd Number: "))

if no1 != 0 and no2 != 0 :
    if no1 > no2 :
        dif = no1 - no2
        print(abs(dif))
    elif no2 > no1 :
        dif = no2 - no1
        print(abs(dif))
    elif no1 == no2 :
        print("Both Are Same")
else :
    print("only +ve Nubers Are Allowed")