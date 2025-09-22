class A:
    def __init__(self):
        self.x = 19

class B(A):
    def __init__(self):
        super().__init__()  # Вызываем конструктор родительского класса
        self.y = self.x + 7  # Используем x из родительского класса


# Создаем объект класса B
obj_b = B()

# Проверяем значения атрибутов
print(f"x = {obj_b.x}")  # x = 10 (из класса A)
print(f"y = {obj_b.y}")  # y = 15 (x + 5)