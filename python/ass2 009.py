hel = eval(input("no of days classes held: "))
att = eval(input("no of days attended : "))

med = input("do you have any medical causes (Y/N):")
medd = med.lower()
per = (att/hel)*100

if per > 75 :
    print("Your Allowed To The Exam")
elif per < 75 and med=='y' :
    print("Your Allowed Under Exception")
else :
    print("Your Not Allowed To the Exam") 