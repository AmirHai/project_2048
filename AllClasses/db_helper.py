# этот класс мне нужен чтобы разобраться во всех ошибках проги
# с помощью него я смотрю на все ошибки и проблемы с базой данных
# отсюда строки кода не брать во внимание и не трогать. они мне нужны для проверки
import sqlite3

with sqlite3.connect('profiles_db.db') as db:
    cursor = db.cursor()
    query = ''' CREATE TABLE profiles(login TEXT, status TEXT, nickname TEXT, bestRecord INTEGER) '''
    cursor.execute(query)
