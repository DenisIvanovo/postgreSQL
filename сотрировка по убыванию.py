"""
Сортировка по алфавиту, в порядке УБЫВАНИЮ.
"""

import psycopg2
from psycopg2 import Error

try:
    # Подключаемся к существующей базе данных.
    connection = psycopg2.connect(user='postgres',
                                  password='fegBCXtf8',
                                  host='localhost',
                                  port='5432',
                                  database='_db')
    print('Мы удачно подключились к базе данных.')
    cursor = connection.cursor()

    ORDER_BY_DESC = """ SELECt country from data_shop
                        ORDER BY country DESC """

    # Выполнение команды: получение информации из нескольких столбцов
    cursor.execute(ORDER_BY_DESC)
    record = cursor.fetchall()
    print('В цикле выходными данными являются полученные данные ')
    for i in record:
        print(i[0])

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")