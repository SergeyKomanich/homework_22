num_month = int(input('Введите номер месяца (1-12): '))


def season(num_m):
    if num_m == 12 or 1 <= num_m <= 2:
        return 'Зима'
    elif 3 <= num_m <= 5:
        return 'Весна'
    elif 6 <= num_m <= 8:
        return 'Лето'
    elif 9 <= num_m <= 11:
        return 'Осень'
    else:
        return 'Введенное вами число не соответствует количеству месяцем!'


print(num_month, '-й месяц - это', season(num_month))
