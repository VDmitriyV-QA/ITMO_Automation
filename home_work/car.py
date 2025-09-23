class Car:
    def __init__(self, color="неизвестен", type="неизвестен", year="неизвестен"):
        """Конструктор класса Car"""
        self.color = color
        self.type = type
        self.year = year

    def start_engine(self):
        """Запуск автомобиля"""
        print("Автомобиль заведен")

    def stop_engine(self):
        """Отключение автомобиля"""
        print("Автомобиль заглушен")

    def set_year(self, year):
        """Присвоение года выпуска"""
        self.year = year
        print(f"Год выпуска установлен: {year}")

    def set_type(self, car_type):
        """Присвоение типа автомобиля"""
        self.type = car_type
        print(f"Тип автомобиля установлен: {car_type}")

    def set_color(self, color):
        """Присвоение цвета автомобиля"""
        self.color = color
        print(f"Цвет автомобиля установлен: {color}")

    def get_info(self):
        """Дополнительный метод для вывода информации об автомобиле"""
        return f"Автомобиль: {self.color} {self.type} {self.year} года"



if __name__ == "__main__":

    my_car = Car("красный", "седан", 2020)


    my_car.start_engine()
    my_car.stop_engine()


    my_car.set_color("синий")
    my_car.set_type("хэтчбек")
    my_car.set_year(2022)

    print(my_car.get_info())