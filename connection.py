"""
Поключение к СУБД и создание базы данных в PostgreSQL
"""
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def new_db():
    cur = con.cursor()  # Этот объект cursor используется для фактического выполнения ваших команд.
    sql_create_database = 'create database _db'  # Пишем команду.
    cur.execute(sql_create_database)  # Передаем команду для выполнения.
    print('База данных создана.')
    cur.close()
    con.close()
    print("Соединение с PostgreSQL закрыто")


try:
    # Подключение к существующей базе данных
    con = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="fegBCXtf8",
        host="127.0.0.1",
        port="5432"
        )
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    print('Удачно подключились к базе данных.')
    new_db()
except (Exception, Error) as error:

    print("Ошибка при работе с PostgreSQL", error)
