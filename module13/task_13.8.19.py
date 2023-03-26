quantity = int(input('Введите количество необходимых билетов '))
total = 0
for i in range(quantity):
    age = int(input('Введите возраст посетителя '))
    if age < 18:
        total += 0
    elif 18 <= age < 25:
        total += 990
    elif age >= 25:
        total += 1390
if quantity > 3:
    print(total * 0.9)
else:
    print(total)