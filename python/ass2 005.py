print("\t\t\t\t\t WELCOME TO THE DEPARTEMENTAL STORE")
bill = eval(input("Enter Total Bill Amount: "))
if bill > 1000 :
    bon = bill * 0.1
    amt = bill - bon
    print(f"Final Amount Is : {amt}") 
else :
    bon = bill * 0.05
    amt = bill - bon
    print(f"The Final Amount Is :{amt}")