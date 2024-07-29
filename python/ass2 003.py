sal = int(input("Enter Your Salary : "))
exp = eval(input("Enter Your Servece Years : "))

if sal <= 5 :
    bon = sal * 0.1
    print(f"Your Bonus Salary Is : Rs.{bon}")
else :
    print("No Bonus For Now")