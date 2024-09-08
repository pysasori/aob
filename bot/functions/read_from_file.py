import os

from config import FILENAME, DEFAULT_NUMBER


def write_to_file(number, filename=FILENAME):
    with open(filename, 'w') as file:
        file.write(str(number))


def read_from_file(filename=FILENAME, default_number=DEFAULT_NUMBER):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return int(file.read())
    else:
        # Если файла нет, создаем его с числом по умолчанию
        write_to_file(filename, default_number)
        return default_number
