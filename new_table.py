"""
Создание таблицы PostgreSQL
"""

import psycopg2
from psycopg2 import Error


class New_table:
    def __init__(self):
        try:
            # Подключаемся к существующей базе данных.
            self.connection = psycopg2.connect(user='postgres',
                                          password='fegBCXtf8',
                                          host='localhost',
                                          port='5432',
                                          database='_db')
            print('Мы удачно подключились к базе.')
            # Создаем курсор для выполнения операций с базой данных.
            self.cursor = self.connection.cursor()
            # Пишем запрос SQL
            create_table_query = '''CREATE TABLE avto
                                                  (ID INT PRIMARY KEY     NOT NULL,
                                                  MODEL           TEXT    NOT NULL,
                                                  PRICE         REAL); '''
            # Выполнение команды: это создает новую таблицу
            self.cursor.execute(create_table_query)
            self.connection.commit()
            print("Таблица успешно создана в PostgreSQL")

        except (Exception, Error)as error:
            print('Ошибка с подключение к базе данных.')

        finally:
            print('Соединение закрыто')



a1 = New_table()