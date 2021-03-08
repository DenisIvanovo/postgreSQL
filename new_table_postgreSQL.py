"""
Создание таблицы PostgreSQL
"""

import psycopg2
from psycopg2 import Error

try:
    # Подключаемся к существующей базе.
    connection = psycopg2.connect(user='postgres',
                                  password='fegBCXtf8',
                                  host='localhost',
                                  port='5432',
                                  database='_db')
    print('Удачное подключения к базе.')
    # Создаем курсор для выполнения операцийй с базой данных.
    cursor = connection.cursor()
    # Пишем запрос SQL
    create_table_query = ''' create table data_den (
	                                                id bigserial PRIMARY KEY ,
	                                                first_name VARCHAR(50) NOT NULL ,
	                                                last_name VARCHAR(50) NOT NULL,
	                                                phone VARCHAR(20) NOT NULL,
	                                                email VARCHAR(50),
	                                                gender VARCHAR(6) NOT NULL,
	                                                job VARCHAR(50) NOT NULL,
	                                                country VARCHAR(50) NOT NULL 
                                                        );'''
    # Выполнение команды: это создает новую таблицу
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица успешно создана в PostgreSQL")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
