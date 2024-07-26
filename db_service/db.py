import sqlite3
from sqlite3 import Error


class Db:
    def __init__(self):
        self.conn = None

    def create_connection(self, db_file):
        try:
            self.conn = sqlite3.connect(db_file)
            try:
                self.conn.execute('DELETE FROM text')
            except Error as e:
                print(e)
            try:
                self.conn.execute('CREATE TABLE IF NOT EXISTS text (id INTEGER PRIMARY KEY, body TEXT)')
            except Error as e:
                print(e)
            self.conn.commit()
        except Error as e:
            print(e)
        finally:
            if self.conn:
                self.conn.close()

    def open_connection(self, db_file):
        try:
            self.conn = sqlite3.connect(db_file)

            return True

        except Error as e:
            print(e)
        return False

    def close_connection(self):
        try:
            self.conn.close()
        except Error as e:
            print(e)

    def insert_text_sentence(self, text):
        try:
            self.conn.execute('INSERT INTO text(body) values(?)', (text,))
            self.conn.commit()
        except Error as e:
            print(e)
        pass