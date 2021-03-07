"""
Получаем данные из базы данных..
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

    select_info = """ SELECT * from Users"""

    # Выполнение команды: получение данных из базы данных
    cursor.execute(select_info)
    record = cursor.fetchall()
    print('Получены данные из базы данных ')
    # В цикле выходными данными являются полученные данные
    for i in record:
        print(i)

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")