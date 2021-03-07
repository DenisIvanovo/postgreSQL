"""
Получаем данные из одной колонки..
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

    insert_query = """ SELECT nic from den"""

    # Выполнение команды: получение данных из одной определеной колонки
    cursor.execute(insert_query)
    record = cursor.fetchall()
    print('В цикле выходными данными являются полученные данные ')
    for i in record:
        print(i)

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")