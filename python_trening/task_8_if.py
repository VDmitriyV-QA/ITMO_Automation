# num = 0
# #
# #
# # if num >= 0:
# #     print('Число больше либо равно 0')
# # else:
# #     print('Число отрицательное')


def task_yes_no(str_1, str_2):
    if str_1 in str_2:
        print("Да")
    else:
        print("Нет")


task_yes_no(str_1="test", str_2="test1")