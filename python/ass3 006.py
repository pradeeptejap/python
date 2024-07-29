numbers = []

print("Please enter 10 numbers:")

for i in range(10):
    num = eval(input(f"Enter number {i+1}: "))
    numbers.append(num)
 
max_number = max(numbers)

print(f"The largest number is: {max_number}")
