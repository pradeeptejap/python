per = eval(input("enter ur age: "))
gen = input("enter ur gender(M/F): ")
mar = input("Status Of Living(Single/Married): ")

genn = gen.lower
marr = mar.lower

if mar == 'married' :
    print("Your Eligible For Bonus")
elif marr == 'single' and genn =='m' and per > 30 :
    print("Your Eligible For Bonus")
elif marr == 'single' and genn =='f' and per > 25 :
    print("your eligible for bonus")
else :
    print("your not eligible for bonus")