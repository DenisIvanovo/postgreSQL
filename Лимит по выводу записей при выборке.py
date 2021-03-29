"""
Лимит по выводу записей при выборке
"""


import json
import psycopg2
from psycopg2 import Error


# Параметры для подключения к базе данных.
with open('info_db.json')as file:
    data = json.load(file)

# Подключаемся к существующей базе данных.
try:
    connection = psycopg2.connect(
                                    user=data['user'],
                                    password=data['password'],
                                    port=data['port'],
                                    host=data['host'],
                                    database=data['database'])

    print('Удачное подключение к базе данных.')
    # Создаем курсор для работы с базой данных.
    cursor = connection.cursor()
    # Пишем команду на выполнение.
    select_limit = """ SELECT * FROM data_shop limit 10
                    """
    # Выполнение команды.
    cursor.execute(select_limit)
    result = cursor.fetchall()
    # Если результат пустой
    if not result:
        print('В базе данных таких записей обнаружено не было.')
    else:
        for i in result:
            print(i)

except (Exception, Error)as error:
    print('Ошибка при подключению к базе данных.', error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print('Соединение с базой данных закрыто')