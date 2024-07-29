leap = eval(input("Enter A Year :"))

if leap % 4 == 0 and leap % 100 != 0 :
    print("It's A Leap Year")
elif leap % 400 :
    print("It's A Leap Year")
else :
    print("It's Not a Leap Year")