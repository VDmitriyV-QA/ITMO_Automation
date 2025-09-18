def task_1() -> None:
    # Создаем переменные с произвольными названиями и задаными типами
    number_int: int = 42
    pi_value: float = 3.14
    greeting: str = "Привет"
    fruits: list = ["яблоко", "банан", "киви"]
    is_active: bool = True

    # Выводим тип каждого из переменных
    print(type(number_int))
    print(type(pi_value))
    print(type(greeting))
    print(type(fruits))
    print(type(is_active))

# Вызов функции
task_1()


def task_2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21]
    # Выводим первые 3 значения списка
    print(a[:3])

# Вызов функции
task_2()


def task_3(number: float) -> float:
    return number ** 2

# Вызов функции с примером
result = task_3(5)
print(result)