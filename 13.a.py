#Чернеги Вікторії   Б19_д/122Б
#Програма виводить на екран користувача дані про місткість в послідовності пар 'ra' і 'ar', видаляючи все, що після крапки.

while True:

    a = input('Write your sequence with dots: ')
    a = a.partition('.')[0]
    for i in range(len(a)):
        if (a[i] == 'a' and a[i + 1] == 'r'):
            print(f'There is "ar" in {a}')
        elif (a[i] == 'r' and a[i + 1] == 'a'):
            print(f'There is "ra" in {a}')
        else:
            print(f'there is no "ra" or "ar" in {a}')

    answer = input('Restart? Yes - 1. No - other.')
    if answer == '1':
        continue
    else:
        break