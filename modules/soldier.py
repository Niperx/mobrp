import sqlite3
from datetime import datetime


def check_count(user_id):  # кол-во солдат на текущем пользователе
    conn = sqlite3.connect('db/main.db')
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM users WHERE user_id = ?", (user_id,))
    count = cur.fetchall()[0][0]
    return count


def check_state(user_id):  # проверка состояния персонажа
    conn = sqlite3.connect('db/main.db')
    cur = conn.cursor()
    cur.execute("SELECT state FROM users WHERE user_id = ?", (user_id,))
    state = cur.fetchone()[0]
    return state


def create_soldier(user_id, name):  # создание нового солдата для профиля
    health, attack, mood, skill, stamina, exp, state = 50, 20, 0, 0, 30, 0, 'menu'
    user_info = (user_id, name, health, attack, mood, skill, stamina, exp, state, datetime.now())
    conn = sqlite3.connect('db/main.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES(?,?,?,?,?,?,?,?,?,?);", user_info)
    conn.commit()


def load_soldier(user_id):  # загрузка всей инфы о солдате
    conn = sqlite3.connect('db/main.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    result = cur.fetchone()
    return result


def delete_soldier(user_id):  # удаление солдата с профиля
    conn = sqlite3.connect('db/main.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
    cur.execute("DELETE FROM users_inventory WHERE owner_id = ?", (user_id,))
    conn.commit()


def get_rank(xp):  # перевод опыта в звание
    if 0 <= xp <= 100:
        rank = 'рядовой'
    elif 101 <= xp <= 225:
        rank = 'ефрейтор'
    elif 226 <= xp <= 375:
        rank = 'мл. сержант'
    elif 376 <= xp <= 550:
        rank = 'сержант'
    elif 551 <= xp <= 750:
        rank = 'ст. сержант'
    elif 751 <= xp <= 975:
        rank = 'старшина'
    elif 976 <= xp <= 1225:
        rank = 'прапощик'
    elif 1226 <= xp <= 1500:
        rank = 'ст. прапощик'
    else:
        rank = False
    return rank


class Soldier:

    def __init__(self, info):
        self.user_id = info[0]
        self.name = info[1]
        self.health = info[2]  # бустится аптечкми и т.п.
        self.attack = info[3]  # бустится оружием и т.п.
        self.mood = info[4]
        self.skill = info[5]
        self.stamina = info[6]
        self.exp = info[7]
        self.state = info[8]
        self.reg_time = info[9]

    def get_info(self):
        print(f'Имя: {self.name}')
        print(f'Здоровье: {self.health}')
        print(f'Атака: {self.attack}')
        print(f'Звание: {self.exp}')
        print(f'Стадия: {self.state}')

    def upload_info(self):  # обновление инфы солдата в бд
        conn = sqlite3.connect('db/main.db')
        cur = conn.cursor()
        cur.execute(
            "UPDATE users SET name = ?, health = ?, attack = ?, mood = ?, skill = ?, stamina = ?, rank = ?, state = ? WHERE user_id = ? ",
            (self.name, self.health, self.attack, self.mood, self.skill, self.stamina, self.exp, self.state,
             self.user_id,))
        conn.commit()


def main():
    pass


if __name__ == "__main__":
    main()
