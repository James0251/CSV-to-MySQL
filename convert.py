import csv
import ast
import re

# Создаем функцию чтения файла, указываем параметры: файл, режим чтения, кодировку
with open('inputFile.csv', 'r', encoding='utf-8', newline='') as file:
    # Создаем функцию записи файла, указываем параметры
    with open('outputFile.csv', 'w', encoding='utf-8', newline='') as wfile:
        # Создаем reader для чтения, ставим разделитель ";"
        reader = csv.reader(file, delimiter=";")
        # Создаем writer для записи
        writer = csv.writer(wfile, delimiter=';')
        # Создаем заголовки (первая строчка), отделяем ее от остальных методом next()
        header = next(reader)
        # Записываем header в исходящий файл example.py
        writer.writerow(header)
        # Проходимся циклом по ридеру
        for line in reader:
            # Преобразуем данные из списка в строку str(line), ищем разделитель ***z0x***, меняем его на ', '
            # Преобразуем данные обратно в список с помощью ast.literal_eval()
            line = ast.literal_eval(re.sub('\*\*\*z0x\*\*\*', '\', \'', str(line)))
            # записываем остальные данные
            writer.writerow(line)
            # Проверяем вывод по столбцам
            print(line[1])
        #     Проверяем количество элементов в header'е
        print(len(header))
    #     Проверяем, выводятся ли остальные значения header'а
    print(header[1])
