fruit = ('Apple', 'Banana', 'Mango', 'Grapes', 'Orange')
juice = tuple(fruit + " Juice" for fruit in fruit)
for i in range(0,4):
    print(juice[i])
