#1 блок
x = 38

print('Приветствую!')
if x < 0:
    print('Меньше нуля')
print('До свидания!')

#2 блок
a, b = 10, 5

if a > b:
    print('a > b')

if a > b and a > 0:
    print('Успех')

if (a > b) and (a > 0 or b < 1000):
    print('Успех')

if 5 < b and b < 10:
    print('Успех')

#3 блок
if '34' > '123':
    print('Успех')

if '123' > '12':
    print('Успех')

if [1, 2] > [1, 1]:
    print('Успех')

#4 блок
if '6' > 5:
    print('Успех')

if [5, 6] > 5:
    print('Успех')

if '6' != 5:
    print('Успех')
