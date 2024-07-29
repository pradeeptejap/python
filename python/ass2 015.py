sub1 = eval(input("Enter Subject 1 Marks: "))
sub2 = eval(input("Enter Subject 2 Marks: "))
sub3 = eval(input("Enter Subject 3 Marks: "))

tot = sub1 + sub2 + sub3
avg = tot/3

if avg > 60 :
    print("Your In Grade A :) \n congrats")
elif avg < 60 and avg >= 50:
    print("Your In Grade B :) \n Well Tried")
elif avg < 50 and avg >= 40:
    print("Your In Grade C :) \n Better but Not Enough")
elif avg < 40 :
    print("Your Failed :( \n Better Luck Next Time") 