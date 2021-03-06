""""
Удаление колонки из таблицы.
Обновляем структуру таблицы.
"""

import psycopg2
import json
from psycopg2 import Error


# основные параметры подключения к базе данных.
with open('info_db.json')as file_info:
    data = json.load(file_info)


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
    # Удаляем колонку day
    drop_column = """ALTER TABLE test
                    DROP COLUMN day;"""
    # Выполнение команды
    cursor.execute(drop_column)
    connection.commit()
    print('Колонка удачно удалена из таблицы.')
except (Exception, Error) as error:
    print('Ошибка подключения к базе данных', error)
finally:
    # Закрываем соединеине с базой.
    if connection:
        cursor.close()
        connection.close()
        print('Соединение с базой данных закрыто.')
