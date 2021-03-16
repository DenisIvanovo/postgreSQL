import csv
import psycopg2
from psycopg2 import Error


def csv_file(columns, data, hath):
    # в функцию передаем 3 параметра(1-инфо,2-инфо,3-путь )
    if len(columns) == 0:
        with open(hath[:-3]+'txt', 'w')as info_file:
            info_file.write('Информация по колонкам отсутствует из таблицы ')
    else:
        with open(hath, 'w', newline='')as file:
            writer = csv.writer(file, delimiter=';')
            # Указываем название колонок в файле.
            writer.writerow([columns[1][0], columns[2][0], columns[3][0], columns[4][0], columns[5][0],
                            columns[6][0], columns[7][0]])

            for d in data:
                try:
                    # Через цикл записываем информацию в колонки.
                    writer.writerow([d[1], d[2], d[3], d[4], d[5], d[6], d[7]])
                except Error:
                    pass


def column_names(cursor):
    try:
        # мы получаем все имена колонок у таблицы.
        insert_query = """SELECT column_name
                                FROM information_schema.columns
                                WHERE table_schema = 'public'
                                AND table_name   = 'data_shop';"""

        # Выполнение команды
        cursor.execute(insert_query)
        return cursor.fetchall()
    except Error:
        # Если ошибка при получении данных ,отправляем пустой список
        return []


def table_data(cursor):
    try:
        # Получаем данные по запросу.
        select = """ SELECt * from data_shop """

        # Выполнение команды: получение информации из нескольких столбцов
        cursor.execute(select)
        return cursor.fetchall()
    except Error:
        # Если ошибка при получении данных ,отправляем пустой список
        return []


def request_db(connection):
    cursor = connection.cursor()
    # В первом запросе мы получаем все имена колонок у таблицы.

    response_to_the_first_request = column_names(cursor)  # ответ на первый запрос
    # В втором запросе мы получем все содержимое из таблицы.
    data = table_data(cursor)  # ответ на второй запрос
    # Полученые данные отправляем для записи в файл.
    # в функцию передаем 3 параметра(1-инфо,2-инфо,3-путь )
    hath = 'E:/den.csv'
    columns = response_to_the_first_request
    csv_file(columns, data, hath)


def main():
    try:
        # Подключаемся к существующей базе данных.
        connection = psycopg2.connect(user='postgres',
                                      password='fegBCXtf8',
                                      host='localhost',
                                      port='5432',
                                      database='_db')
        print('Мы удачно подключились к базе данных.')
        # пишем и отправляем запрос на исполнение
        request_db(connection)

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            connection.close()
            print("Соединение с PostgreSQL закрыто")


if __name__ == '__main__':
    main()
