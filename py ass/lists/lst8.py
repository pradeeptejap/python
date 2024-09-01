fruits = ('Apple', 'Banana', 'Mango', 'Apple', 'Orange')
fruit = 'Apple'

if fruit in fruits:
    count = fruits.count(fruit)
    print(f"{fruit} exists and appears {count} times.")
    print()
else:
    print(f"{fruit} does not exist in the tuple.")
