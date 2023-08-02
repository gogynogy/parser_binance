import sqlite3

from messages.start_message import give_time
from notify_admins import write_admin


class SQL:
    def __init__(self):
        """Initializing Database Connection"""
        self.conn = sqlite3.connect("clients.db")
        self.cursor = self.conn.cursor()

    def checkDB(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS `Users` (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            userid TEXT,
            user_name TEXT
            )""")
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
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS `Agents` (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegramID TEXT,
            TelegramNikName TEXT,
            Balance INT NOT NULL DEFAULT 0,
            Percent INT,
            BinancePayID TEXT,
            TRC20 TEXT
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
                self.cursor.execute('''UPDATE ToDo SET Count = (Count + 1) WHERE TelegramNikName = ?''', (username, ))
        except sqlite3.Error as error:
            print(f"Ошибка при работе с SQLite CheckAccount {error}")
        finally:
            self.conn.commit()

    def CheckAgent(self, telegramNickName):
        try:
            self.cursor.execute("SELECT * FROM Agents WHERE TelegramNikName = (?)", (telegramNickName,))
            agent = self.cursor.fetchone()
            if not agent:
                self.cursor.execute("SELECT * FROM Agents WHERE Id = (?)", (telegramNickName,))
                agent = self.cursor.fetchone()
            return agent
        except sqlite3.Error as error:
            print(f"Ошибка при работе с SQLite CheckAgent {error}")
        finally:
            self.conn.commit()

    def AddAgent(self, telegramID, username, percent):
        try:
            self.cursor.execute(f"INSERT INTO Agents (telegramID, TelegramNikName, Percent) VALUES (?, ?, ?)",
                                (telegramID, username, percent))
        except sqlite3.Error as error:
            print(f"Ошибка при работе с SQLite AddAgent {error}")
        finally:
            self.conn.commit()

    def GiveAgents(self):
        try:
            self.cursor.execute("SELECT * FROM Agents")
            agents = self.cursor.fetchall()
            return agents
        except sqlite3.Error as error:
            print(f"Ошибка при работе с SQLite GiveAgents {error}")
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
            self.cursor.execute("SELECT * FROM Orders ORDER BY Id DESC LIMIT 1")
            count = self.cursor.fetchone()
            return count[0]
        except sqlite3.Error as error:
            print(f"Ошибка при работе с SQLite make_order {error}")
        finally:
            self.conn.commit()

    def watch_open_orders(self):
        try:
            self.cursor.execute("SELECT * FROM Orders WHERE Done = (?)", ('NO',))
            text = "\n".join([f'@{user[2]} на {user[4]} LKR в городе {user[3]}' for user in (self.cursor.fetchall())])
            return text
        except sqlite3.Error as error:
            print(f"Ошибка при работе с SQLite watch_open_orders {error}")
        finally:
            self.conn.commit()