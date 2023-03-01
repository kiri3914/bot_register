import csv 
# импортируем модуль csv для работы с CSV-файлами

def create_table():
    # создаем функцию для создания таблицы в CSV-файле

    fields = ['first_name', 'last_name', 'phone', 'chat_id']
    # создаем список полей для таблицы

    with open('names.csv', 'w', newline='') as csvfile:
        # открываем файл names.csv в режиме записи ('w') и создаем объект csvfile
        # newline='' нужен для того, чтобы не было пустых строк между записями в файле

        writer = csv.DictWriter(csvfile, fieldnames=fields)
        # создаем объект DictWriter для записи словарей в CSV-файл
        # указываем список полей fields

        writer.writeheader()
        # записываем заголовок в файл

def insert_table(**kwargs):
        with open('names.csv', 'a', newline='') as csvfile:
            # открываем файл names.csv в режиме добавления ('a')
            # newline='' нужен для того, чтобы не было пустых строк между записями в файле

            fields = ['first_name', 'last_name', 'phone', 'chat_id']
            # создаем список полей для таблицы

            writer = csv.DictWriter(csvfile, fieldnames=fields)
            # создаем объект DictWriter для записи словарей в CSV-файл
            # указываем список полей fields

            writer.writerow(kwargs)
            # записываем словарь kwargs в CSV-файл




def get_chats() -> list:
    # создаем функцию для вставки данных в таблицу

    with open('names.csv', 'r') as file:
        # открываем файл names.csv в режиме чтения ('r')

        reader = csv.reader(file, delimiter=';')
        # создаем объект reader для чтения CSV-файла
        # указываем разделитель ';'

        if list(reader) == []:
            # если файл пустой, то создаем таблицу

            create_table()
            
    # Открываем файл
    with open('names.csv', 'r') as file:
        # Создаем объект reader, используя разделитель ","
        reader = csv.reader(file, delimiter=',')
        # Читаем данные
        try:
            return [i[3] for i in reader]
        except:
            return []    

def check_user(chat_id: int) -> bool:
    if str(chat_id) in get_chats():
        return True
    return False


