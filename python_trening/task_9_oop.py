from task_9_checks import Checks

class BaseButton(Checks):
    type = 'Кнопка'

    def __init__(self, text, link):
        self.text = text
        self.link = link
        super().__init__('button.' + text.lower())


# Создаем экземпляры класса
home = BaseButton('Домой', '/home')
catalog_msk = BaseButton('Каталог', '/msk/catalog')

# Получаем доступ к атрибутам
print(home.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

print('\n')

print(catalog_msk.text)
print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)


class ButtonTwo(Checks):

    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        super().__init__(loc)

    def click(self):
        return 'Клик по локатору - {}'.format(self.loc)


# Создаем экземпляры класса
home_two = ButtonTwo('Домой', '/home', 'button#home')

# Вызываем метод
print(home_two.click())


class Input(Checks):
    def __init__(self, loc, text):
        self.text = text
        super().__init__(loc)


class Button(Checks):
    def __init__(self, loc, text):
        self.text = text
        super().__init__(loc)


class Title(Checks):
    def __init__(self, loc, text):
        self.text = text
        super().__init__(loc)


class Link(Checks):
    def __init__(self, loc, text):
        self.text = text
        super().__init__(loc)


# Создаем объекты для каждого класса
search_input = Input('input#search', 'Поле поиска')
submit_button = Button('button#submit', 'Отправить')
main_title = Title('h1.main', 'Главная страница')
home_link = Link('a#home', 'Домой')


# Выводим на консоль text и loc каждого объекта
print("Input:")
print(f"Loc: {search_input.loc}")
print(f"Text: {search_input.text}")
print()

print("Button:")
print(f"Loc: {submit_button.loc}")
print(f"Text: {submit_button.text}")
print()

print("Title:")
print(f"Loc: {main_title.loc}")
print(f"Text: {main_title.text}")
print()

print("Link:")
print(f"Loc: {home_link.loc}")
print(f"Text: {home_link.text}")

print("\n" + "="*50)
print("Результаты вызова метода check_text():")
print("="*50)

# Вызываем метод check_text() для каждого объекта
print(f"home.check_text(): {home.check_text()}")
print(f"catalog_msk.check_text(): {catalog_msk.check_text()}")
print(f"home_two.check_text(): {home_two.check_text()}")
print(f"search_input.check_text(): {search_input.check_text()}")
print(f"submit_button.check_text(): {submit_button.check_text()}")
print(f"main_title.check_text(): {main_title.check_text()}")
print(f"home_link.check_text(): {home_link.check_text()}")