"""
Добавляем данные в таблицу.
"""
import psycopg2
from psycopg2 import Error

try:
    # Подключаемся к существующей базе данных.
    connection = psycopg2.connect(user='postgres',
                                  password='fegBCXtf8',
                                  host='localhost',
                                  port='5432',
                                  database='den_shop')
    print('Мы удачно подключились к базе данных.')
    cursor = connection.cursor()
    for i in range(3):
        insert_query = """ INSERT INTO Users ("user", "name", "phote", "email", "password")
                                  VALUES ( 'd', 'denis','89992','md@mail.ru', 3432423)"""

        # Выполнение команды: это создает новую таблицу
        cursor.execute(insert_query)
        connection.commit()
        print("Данные внесены в базу")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")