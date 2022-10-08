import random
import sqlite3
from datetime import datetime


# def create_db():  # Создание таблицы в БД (одноразовая функция)
#     conn = sqlite3.connect('../db/main.db')
#     cur = conn.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS users(
#         user_id INT PRIMARY KEY,
#         name TEXT,
#         health INT,
#         attack INT,
#         mood INT,
#         skill INT,
#         stamina INT,
#         rank TEXT,
#         soldiers_count INT,
#         reg_time TEXT);
#     """)
#     conn.commit()

def check_count(user_id):  # кол-во солдат на текущем пользователе
    conn = sqlite3.connect('db/main.db')
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM users WHERE user_id = ?", (user_id,))
    count = cur.fetchall()[0][0]
    return count


def create_soldier(user_id, name):
    health, attack, mood, skill, stamina, exp = 50, 20, 50, 0, 30, 0
    user_info = (user_id, name, health, attack, mood, skill, stamina, exp, datetime.now())
    conn = sqlite3.connect('db/main.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES(?,?,?,?,?,?,?,?,?);", user_info)
    conn.commit()


def load_soldier(user_id):
    conn = sqlite3.connect('db/main.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    result = cur.fetchone()
    return result


def delete_soldier(user_id):
    conn = sqlite3.connect('db/main.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
    cur.execute("DELETE FROM users_inventory WHERE owner_id = ?", (user_id,))
    conn.commit()


def get_rank(xp):
    if 0 >= xp <= 100:
        rank = 'рядовой'
    elif 101 >= xp <= 225:
        rank = 'ефрейтор'
    elif 226 >= xp <= 375:
        rank = 'мл. сержант'
    elif 376 >= xp <= 550:
        rank = 'сержант'
    elif 551 >= xp <= 750:
        rank = 'ст. сержант'
    elif 751 >= xp <= 975:
        rank = 'старшина'
    elif 976 >= xp <= 1225:
        rank = 'прапощик'
    elif 1226 >= xp <= 1500:
        rank = 'ст. прапощик'
    else:
        rank = False
    return rank


class Soldier:

    def __init__(self, info):
        self.user_id = info[0]
        self.name = info[1]
        self.health = info[2]
        self.attack = info[3]
        self.mood = info[4]
        self.skill = info[5]
        self.stamina = info[6]
        self.exp = info[7]
        self.reg_time = info[8]

    def get_info(self):
        print(f'Имя: {self.name}')
        print(f'Здоровье: {self.health}')
        print(f'Атака: {self.attack}')
        print(f'Звание: {self.exp}')


def main():
    delete_soldier(190112213)


if __name__ == "__main__":
    main()
