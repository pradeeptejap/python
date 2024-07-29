print("\t\t\t\t\t\t EXAMPLE HIGH SCHOOL'S GRADES TIME")

avg = eval(input("Enter Average Marks: ")) #avg variable to stare average marks

# conditions to check grades
if avg > 90 :
    print("Your grade is A+")
elif avg < 90 and avg >= 80 :
    print("Your grade is A")
elif avg < 80 and avg >= 70 :
    print("Your grade is b")
elif avg < 70 and avg >= 60 :
    print("Your grade is c")
elif avg < 50:
    print("Your Failed :( ")
