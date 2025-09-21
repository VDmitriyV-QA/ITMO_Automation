def print_max(a, b):
    print(max(a, b))


print_max(123, -5675)


def check_difference(a, b):
    if abs(a - b) == 135:
        print(f'yes')
    else:
        print(f'no')


check_difference(-135, -270)


def get_season(month):
    if month in [12, 1, 2]:
        print('зима')
    elif month in [3, 4, 5]:
        print('весна')
    elif month in [6, 7, 8]:
        print('лето')
    elif month in [9, 10, 11]:
        print('осень')
    else:
        print('Неверный номер месяца')

get_season(6)


def check_numbers(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print('yes')
    else:
        print('no')


check_numbers(18, 12, 30)


def count_positive_numbers(a, b, c, d, e):
    print(sum(1 for num in (a, b, c, d, e) if num > 0))


count_positive_numbers(6, 8, -2, 15, -1)


def calculate_days(years, months):
    total_days = years * 12 * 29 + months * 29
    print(f'Количество дней: {total_days}')


calculate_days(2, 12)