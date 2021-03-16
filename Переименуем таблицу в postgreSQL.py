"""
Изменяем название таблицы.
Обновляем структуру таблицы.
"""

import json
import psycopg2
from psycopg2 import Error

# основные параметры подключения к базе данных.
with open('info_db.json')as info_file:
    data = json.load(info_file)

# Подключаемся к актульной базе данных.
try:
    connection = psycopg2.connect(user=data['user'],
                                  password=data['password'],
                                  port=data['port'],
                                  host=data['host'],
                                  database=data['database'])
    print('Успешное подключение к базе данных')
    # Создаем курсор для манипуляции с базой данных.
    cursor = connection.cursor()
    # Пишем запрос для выполнения команды.
    # Переименуем таблицу avto
    add_column = """ALTER TABLE avto RENAME TO avto_new;"""
    # Выполнение команды
    cursor.execute(add_column)
    connection.commit()
    print('Таблица переименована.')
except (Exception, Error) as error:
    print('Ошибка подключения к базе данных', error)
finally:
    # Закрываем соединеине с базой.
    if connection:
        cursor.close()
        connection.close()
        print('Соединение с базой данных закрыто.')