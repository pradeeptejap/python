bill = eval(input("Enter Bill Amount: "))
method = input("Enter Payment Method: ")

met = method.lower()
if method == 'cash' :
    dis = bill * 0.25
    amt = bill - dis
    print("Your Final Amount Is :",amt)
elif method == 'credit' :
    dur = eval(input("Enter The Dilay Of Payment: "))
    if dur < 7 :
        dis = bill * 0.15
        amt = bill - dis
        print("Your Final Amount Is: ",amt)
    elif dur > 7 :
        dis = bill * 0.1
        amt = bill + dis
        print("Your Final Amount With Penalty: ",amt)