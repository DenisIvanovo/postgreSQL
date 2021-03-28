"""
Удаеление заданых записей
Удаляем используя шаблон - LIKE
Удаляються все записи совподая с шаблоном

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
    delete_data = """ DELETE FROM data_shop
                        where email like '%@webs.com'
                    """
    # Выполнение команды.
    cursor.execute(delete_data)
    connection.commit()
    print('Команда выполнена, все записи удалены.')

except (Exception, Error)as error:
    print('Ошибка при подключению к базе данных.', error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print('Соединение с базой данных закрыто')