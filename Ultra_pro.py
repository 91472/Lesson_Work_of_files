# Урок: Работа с файлами. Кодировки, сериализация данных, json
# Задание Ultra-Pro:
# 1. Выполните задание уровня pro
# 2. В подпрограмме “Личный счет” добавьте сохранение суммы счета в файл, при следующем открытии программы
# прочитайте сумму счета, которую сохранили
# 3. В подпрограмме “Личный счет” добавьте сохранение истории покупок в файл, при следующем открытии программы
# прочитайте историю и новые покупки уже добавляйте к ней

# Выполнение задания Pro:
#1. Задание уровня Pro выполнено, файл Pro.py с исходным кодом сохранен в корневую директорию с проектом.
"""
note_Ultra_pro.png - Скрин от кураторов УИИ с пояснениями и дополнениями по формулировке последующих двух заданий
"""
# 2. В подпрограмме “Личный счет” добавьте сохранение суммы счета в файл, при следующем открытии программы
# прочитайте сумму счета, которую сохранили
# 3. В подпрограмме “Личный счет” добавьте сохранение истории покупок в файл, при следующем открытии программы
# прочитайте историю и новые покупки уже добавляйте к ней

#Работоспособность программы протестирована только при запуске из IDE Pycharm и терминала командной строки ОС Windows 10
#импортируем необходимые библиотеки:
from time import sleep
import datetime
import os
import pandas as pd
import csv
#создаем бесконечный цикл while, создаем ряд функций, алгоритм работы программы в точности совпадает с описанием note_Ultra_pro.png
while True:
    def account_balance():
        with open('account_balance.txt', 'w') as f:
            with open('my_account.csv') as f1:
                reader = csv.reader(f1)
                sum_fill_up = 0
                sum_fill_down = 0
                f1.seek(149, 0)
                for row in reader:
                    sum_fill_up += int(row[0])
                    sum_fill_down += int(row[2])
                account_balance = sum_fill_up - sum_fill_down
            f.write(str(account_balance))
        return str(account_balance)
# блок кода для очистки экрана терминала (консоли) IDE (имитация очистки), OC Windows, MAC, Linux (реальная очистка)
    def clear():
        print('\n' * 100)  # для "очистки" экрана терминала IDE PyCharm (имитация)
        def cls():
            os.system('cls||clear')  # для очистки экрана терминала ОС Windows, MAC, Linux (реальная очистка)
        cls()
# ОСНОВНОЕ МЕНЮ
    def main_menu():
        clear()
        print('\rОСНОВНОЕ МЕНЮ:\n1 МОЙ СЧЕТ {}\n2 ПОПОЛНИТЬ СЧЕТ\n3 СОВЕРШИТЬ ПОКУПКУ\n4 ИСТОРИЯ ПОКУПОК\n5 ВЫХОД ИЗ ПРОГРАММЫ'.format(account_balance()))
        return int(input('ВВЕДИТЕ НУЖНЫЙ ПУНКТ МЕНЮ: '))
    def my_account_w(balance):
        with open('my_account.csv', 'a', newline = '\n') as f:
            writer = csv.writer(f)
            writer.writerows(balance)

    def my_account_r():
        pd.set_option('display.max_columns', 5)
        pd.set_option('display.width', 2000)
        df = pd.read_csv('my_account.csv')
        print('\r1 МОЙ СЧЕТ {}'.format(account_balance()))
        print(df)
        return input('ДЛЯ ВОЗВРАТА В ОСНОВНОЕ МЕНЮ ВВЕДИТЕ exit: ')

    def fill_up_account():
        print('\r2 ПОПОЛНИТЬ СЧЕТ')
        fill_up_sum = input('ВВЕДИТЕ СУММУ ДЛЯ ПОПОЛНЕНИЯ СЧЕТА (в целочисленном формате, руб.): ')
        balance = [[fill_up_sum, str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")), 0, 0]]
        my_account_w(balance)


    def buying_history_r():
        df = pd.read_csv('buying_history.csv')
        print('\r4 ИСТОРИЯ ПОКУПОК')
        print(df)
        return input('ДЛЯ ВОЗВРАТА В ОСНОВНОЕ МЕНЮ ВВЕДИТЕ exit: ')

    def buying_history_w(buying):
        with open('buying_history.csv', 'a', newline = '\n') as f:
            writer = csv.writer(f)
            writer.writerows(buying)

    def buying():
        print('\r3 СОВЕРШИТЬ ПОКУПКУ')
        buying_sum = int(input('ВВЕДИТЕ СУММУ ПОКУПКИ (в целочисленном формате, руб.): '))
        if int(account_balance()) < buying_sum:
            print('У ВАС НЕДОСТАТОЧНО СРЕДСТВ НА СЧЕТЕ')
            sleep(5)
        else:
            df = pd.read_csv('provisions_list.csv', index_col = 0)
            print(df)
            code = int(input('ВВЕДИТЕ КОД ОДНОЙ ИЗ ГРУПП ПРОДОВОЛЬСТВЕННЫХ ТОВАРОВ: '))
            balance = [[0, 0, buying_sum, str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))]]
            with open('provisions_list.csv') as f:
                provision = list(csv.reader(f))[code][1]
            buying = [[provision, buying_sum, str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))]]
            my_account_w(balance)
            buying_history_w(buying)

    key = main_menu()
    if key == 5:
        clear()
        break
    if key == 1:
        clear()
        key_return = my_account_r()
        while key_return != 'exit':
            clear()
            key_return = my_account_r()
    if key == 2:
        clear()
        fill_up_account()
    if key == 3:
        clear()
        buying()
    if key == 4:
        clear()
        key_return = buying_history_r()
        while key_return != 'exit':
            clear()
            key_return = buying_history_r()