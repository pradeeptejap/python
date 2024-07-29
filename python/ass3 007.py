no = eval(input("Enter a Number: "))
nos = str(no)
let = len(nos)

sum = 0

for i in nos:
    sum += int(i) ** let 

if sum == no:
    print(f"{no} is armstrong")
else :
    print(f"{no} is not an armstrong number")