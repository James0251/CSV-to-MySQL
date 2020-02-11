import csv
import mysql.connector

# Открываем для чтения ранее созданный файл, он нам нужен для создания таблицы и заголовков
with open('outputFile.csv', 'r', encoding='utf-8', newline='') as file:
    # Создаем reader
    reader = csv.reader(file, delimiter=";")
    # Создаем header
    header = next(reader)
    # Делаем проверку вывода данных
    for line in reader:
        a = line
        # print(a) #работает, выводятся все строки, правда без хедера, он остался там..


# Создаем пустую переменную с заголовками, она нам понадобиться для внесения данных в таблицу
header_string = ""
# Создаем пустую переменную, с помощью которой мы создадим заголовки в таблице
header_string_typed = ""
# Пробежимся циклом по header'у, найдем его элементы
for header_item in header:
    # Для добавления в таблицу будем записывать найденные элементы через ','
    header_string += header_item + ","
    # Для создания заголовков таблицы будем к каждому элементу присваивать простой текстовый тип данных
    # Потом, уже в самой таблице этот тип данных можно будет поменять
    header_string_typed += header_item + " VARCHAR(255),"
#     Удаляем последнюю запятую с конца элементов
header_string = header_string.rstrip(",")
# Тоже удаляем последнюю запятую
header_string_typed = header_string_typed.rstrip(",")
# Создаём подключение к БД
mydb = mysql.connector.connect(
    host="localhost",
    user="username",
    passwd="password",
    database="databaseName"  # Изначально этой строки нет, нужно создать базу данных
)
# Создаем курсор для нашей Базы Данных
cur = mydb.cursor(buffered=True)

# Создаем таблицу и указываем в ней поля с помощью интерполяции и переменной header_string_typed
cur.execute(f"CREATE TABLE IF NOT EXISTS tableName ({header_string_typed})")

# Просмотрим созданную таблицу с помощью этих команд
cur.execute("SHOW TABLES")

# Создаем (изначально пустой) счетчик строк
count = 0
# Снова открываем файл для чтения, на этот раз будем работать с заполнением таблицы
with open('outputFile.csv', 'r', encoding='utf-8', newline='') as file:
    # csv_data для чтения, разделитель ';'
    csv_data = csv.reader(file, delimiter=";")
    # пробегаемся циклом по csv_dat'е
    for line in csv_data:
        # Если счетчик меньше нуля
        if count < 1:
            # Прибавляем к нему по строке
            count += 1
        else:
            # Т.к. счетчик будет расти, создаем пустую переменную value_string, которая будет отвечать за
            # значения для header'а
            value_string = ""
            # Ищем элементы значений по строкам
            for value_item in line:
                # Каждое значение заключаем в кавычки и записываем через ","
                value_string += '"' + value_item + '",'
            #     Последнюю запятую удаляем
            value_string = value_string.rstrip(",")
            # Выполняем проверку на вывод значений
            print(value_string)
            # Если всё хорошо, то под каждым элементом header'а записываем его значение
            cur.execute(f"INSERT INTO tableName ({header_string}) VALUES ({value_string})")
            # Прибавляем по строке каждый раз до окончания записей в нашем файле
            count += 1
#             Сохраняем полученный результат
mydb.commit()
# Закрываем курсор
# cur.close()
# Закрываем базу данных
mydb.close()









