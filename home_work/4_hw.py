from car import Car


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self, a=None, b=None):
        a = a if a is not None else self.a
        b = b if b is not None else self.b
        result = a + b
        print(f"Сложение: {a} + {b} = {result}")
        return result

    def multiplication(self, a=None, b=None):
        a = a if a is not None else self.a
        b = b if b is not None else self.b
        result = a * b
        print(f"Умножение: {a} × {b} = {result}")
        return result

    def division(self, a=None, b=None):
        a = a if a is not None else self.a
        b = b if b is not None else self.b
        if b == 0:
            print("Ошибка: деление на ноль!")
            return None
        result = a / b
        print(f"Деление: {a} ÷ {b} = {result}")
        return result

    def subtraction(self, a=None, b=None):
        a = a if a is not None else self.a
        b = b if b is not None else self.b
        result = a - b
        print(f"Вычитание: {a} - {b} = {result}")
        return result


class DemoQAButton:
    def __init__(self, button_text):
        self.text = button_text
        self.type = "Кнопка"
        self.locator = ""

    def click(self):
        return f"Клик по кнопке {self.text}"


def main():

    print("=== ДЕМОНСТРАЦИЯ КЛАССА RECTANGLE ===")
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3, 7)
    rect3 = Rectangle(8, 12)

    print("Прямоугольник 1:")
    print(f"Площадь: {rect1.calculate_area()}")
    print(f"Периметр: {rect1.calculate_perimeter()}\n")

    print("Прямоугольник 2:")
    print(f"Площадь: {rect2.calculate_area()}")
    print(f"Периметр: {rect2.calculate_perimeter()}\n")

    print("Прямоугольник 3:")
    print(f"Площадь: {rect3.calculate_area()}")
    print(f"Периметр: {rect3.calculate_perimeter()}\n")


    print("=== ДЕМОНСТРАЦИЯ КЛАССА MATH ===")
    math_obj = Math(10, 5)
    math_obj.addition()
    math_obj.multiplication()
    math_obj.division()
    math_obj.subtraction()


    math_obj.addition(15, 3)
    math_obj.division(20, 4)
    print()


    print("=== ДЕМОНСТРАЦИЯ КЛАССА DEMOQABUTTON ===")
    buttons_data = [
        "Text Box",
        "Check Box",
        "Radio Button",
        "Web Tables",
        "Buttons",
        "Links",
        "Broken Links - Images",
        "Upload and Download",
        "Dynamic Properties"
    ]

    buttons = [DemoQAButton(text) for text in buttons_data]

    for button in buttons:
        print(f"Текст кнопки: {button.text}")
        print(f"Тип: {button.type}")
        print(f"Локатор: {button.locator}")
        print(button.click())
        print("-" * 30)


    print("=== ДЕМОНСТРАЦИЯ КЛАССА CAR ===")
    car1 = Car("черный", "внедорожник", 2018)
    car1.start_engine()
    car1.set_color("белый")
    car1.set_year(2023)
    print(car1.get_info())
    car1.stop_engine()


if __name__ == "__main__":
    main()