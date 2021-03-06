# Урок: Работа с файлами. Кодировки, сериализация данных, json
# Задание Pro:
#1. Выполните задание уровня light
#2. Замерьте время генерации отчета (время выполнения пункта 3).
#3. В каждый файл из задания Light добавьте параметр: время, затраченное на генерацию отчета.

# Выполнение задания Pro:
#1. Задание уровня light выполнено, файл Lite.py с исходным кодом сохранен в корневую директорию с проектом.

#2. Замерьте время генерации отчета (время выполнения пункта 3).
import time #импортируем модуль для работы со временем
#Время, затраченное на генерацию отчета в формате CSV из задания Lite:
time_start = time.process_time_ns() #фиксируем время начала запуска подпрограммы генерации отчета csv
import csv #импорт билиотеки для работы с форматом csv
with open('cars.txt', newline = '') as f: #открытие файла cars.txt в режиме чтения менеджером контекста
    reader = csv.reader(f) #создание объекта csv с записью в него данных из потока f
    with open('cars.csv', 'w', newline = '') as f1: #открытие файла в режиме записи менеджером контекста
        writer = csv.writer(f1) #создание файла 'cars.csv' в формате данных csv
        writer.writerows(reader) #построчная запись в файл 'cars.csv' данных из файла 'cars.txt' (сериализация)
time.process_csv = time.process_time_ns() - time_start #фиксируем разность времени завершения и начала подпрограммы генерации отчета csv
print('Время, затраченное на генерацию отчета в формате CSV из задания Lite:', time.process_csv, 'ns')

#Время, затраченное на генерацию отчета в формате JSON из задания Lite:
time_start = time.process_time_ns() #фиксируем время начала запуска подпрограммы генерации отчета json
import json #импорт билиотеки для работы с форматом json
with open('cars.txt') as f: #открытие файла cars.txt в режиме чтения менеджером контекста
    data = f.read() #считываение данных методом read в объект data
    with open('cars.json', 'w') as f1: #открытие файла cars.json в режиме записи менеджером контекста
        json.dump(data, f1) #создание и запись данных data в файл cars.json в формате json методом dump (сериализация)
time.process_json = time.process_time_ns() - time_start #фиксируем разность времени завершения и начала подпрограммы генерации отчета json
print('Время, затраченное на генерацию отчета в формате JSON из задания Lite:', time.process_json, 'ns')


#3. В каждый файл из задания Light добавляем параметр: время, затраченное на генерацию отчета.

#Добавление в файл CSV:
with open('cars.csv', 'a') as f: #открытие в режиме добвления менеджером контекста
    writer = csv.writer(f) #создаем объект для записи
    writer.writerows([['time of process report (ns)', str(time.process_csv)]]) #добавляем новый список в конец файла

#Добавление в файл JSON:
with open('cars.json') as f: #открытие в режиме чтения
    data = json.load(f) #десериализация
    data = data+'time of process report (ns),'+str(time.process_json) #конкатенация к объекту новых строковых данных
with open('cars.json', 'w') as f: #открытие в режиме записи
    json.dump(data, f) #перезаписываем файл вновь с дополненной информацией, сериализуем в json