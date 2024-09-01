numbers = set()
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.add(num)

asc = sorted(numbers)
dsc = sorted(numbers, reverse=True)

print("Unique numbers in ascending order:", asc)
print("Unique numbers in descending order:", dsc)
