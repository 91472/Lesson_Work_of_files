# Урок: Работа с файлами. Кодировки, сериализация данных, json
# Задание Lite:
# 1. Выполните задание уровня ultra light
# 2. Создайте csv-файл с данными о машине.
# 3. Создайте json-файл с данными о машине.

# Выполнение задания Lite:
# 1. Задание уровня ultra light выполнено, файл Ultra_lite.py с исходным кодом сохранен в корневую директорию с проектом.

# 2. Создание csv-файла с данными о машинах:
import csv #импорт билиотеки для работы с форматом csv
with open('cars.txt', newline = '') as f: #открытие файла cars.txt в режиме чтения менеджером контекста
    reader = csv.reader(f) #создание объекта csv с записью в него данных из потока f
    with open('cars.csv', 'w', newline = '') as f1: #открытие файла в режиме записи менеджером контекста
        writer = csv.writer(f1) #создание файла 'cars.csv' в формате данных csv
        writer.writerows(reader) #построчная запись в файл 'cars.csv' данных из файла 'cars.txt' (сериализация)
with open('cars.csv', newline = '') as f: #открытие файла cars.csv в режиме чтения менеджером контекста
    reader = csv.reader(f) #считывание данных из файла csv в объект Python (десериализация)
    print('Вывод на экран данных из файла cars.csv классическим методом построчно из объекта reader:\n')
    for row in reader: #построчный перебор объекта reader
        print(row, type(row))

import pandas as pd #импорт библиотеки для работы с объектами Series и DataFrame
df = pd.read_csv('cars.csv') #десериализация (преобразование объекта csv в объект Python)
print('\nСчитывание данных из файла cars.csv и вывод на экран методом Pandas, через создание объекта DataFrame:\n')
print(df)

# 3. Создание json-файла с данными о машинах:
import json #импорт билиотеки для работы с форматом json
with open('cars.txt') as f: #открытие файла cars.txt в режиме чтения менеджером контекста
    data = f.read() #считываение данных методом read в объект data
    with open('cars.json', 'w') as f1: #открытие файла cars.json в режиме записи менеджером контекста
        json.dump(data, f1) #создание и запись данных data в файл cars.json в формате json методом dump (сериализация)
with open('cars.json') as f: #открытие файла cars.json в режиме чтения менеджером контекста
    data = json.load(f) #чтение данных из формата json в исходный формат Python (десериализация)
    print('\nСчитывание данных из файла cars.json и вывод на экран c указанием типа данных:\n')
    print(data, type(data))