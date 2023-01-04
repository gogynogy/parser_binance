import sqlite3

from messages.start_message import give_time
from notify_admins import write_admin


class SQL:
    def __init__(self):
        """Initializing Database Connection"""
        self.conn = sqlite3.connect("clients.db")
        self.cursor = self.conn.cursor()

    def checkDB(self):
        """проверяет наличие базы данных"""
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS `Users` (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            userid TEXT,
            user_name TEXT
            )""")
        self.conn.commit()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS `ToDo` (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            TelegramNikName TEXT,
            Count INT NOT NULL DEFAULT 1
            )""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS `Orders` (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            userid TEXT,
            TelegramNikName TEXT,
            Location TEXT,
            HowMuch INT,
            Time TEXT,
            Done TEXT NOT NULL DEFAULT NO
            )""")
        self.conn.commit()


    def CheckAccount(self, id, username):
        """checks if the id exists in the database"""
        try:
            self.cursor.execute("SELECT userid FROM Users WHERE userid = (?)", (id,))
            if self.cursor.fetchone() is None:
                self.cursor.execute(f"INSERT INTO Users (userid, user_name) VALUES (?, ?)", (id, username))
                self.cursor.execute(f"INSERT INTO ToDo (TelegramNikName) VALUES (?)", (username, ))
            else:
                self.cursor.execute('''UPDATE ToDo SET Count = (Count + 1) WHERE TelegramNikName = ?''',
                                    (username, ))
        except sqlite3.Error as error:
            print(f"Ошибка при работе с SQLite CheckAccount {error}")
        finally:
            self.conn.commit()


    def watch_activity(self):
        try:
            self.cursor.execute("SELECT * FROM ToDo")
            text = "\n".join([f'{user[0]}) @{user[1]} обращений {user[2]}' for user in (self.cursor.fetchall())])
            return text
        except sqlite3.Error as error:
            print(f"Ошибка при работе с SQLite watch_activity {error}")
        finally:
            self.conn.commit()


    def make_order(self, id, username, location, HowMuch):
        try:
            self.cursor.execute(f"INSERT INTO Orders (userid, TelegramNikName, Location, HowMuch, Time)"
                                f" VALUES (?, ?, ?, ?, ?)", (id, username, location, HowMuch, give_time()))
        except sqlite3.Error as error:
            print(f"Ошибка при работе с SQLite make_order {error}")
        finally:
            self.conn.commit()