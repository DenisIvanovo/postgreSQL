
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

    SELECT_3 = """ SELECt * from data_shop
                        where gender = 'Female' AND 
                        (country = 'China' or country = 'Indonesia')
                        ORDER BY country ASC """

    # Выполнение команды: получение информации из нескольких столбцов
    cursor.execute(SELECT_3)
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