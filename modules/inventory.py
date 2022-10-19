import sqlite3
from datetime import datetime


# Проверять наличие солдата в мейн коде, ну и при смерти удалять все предметы
def add_items(user_id, item_id, value=1):
    conn = sqlite3.connect('db/main.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users_inventory WHERE owner_id = ? and item_id = ?", (user_id, item_id,))
    item_info = cur.fetchall()
    if not item_info:
        cur.execute("INSERT INTO users_inventory VALUES(?, ?, ?, ?);",
                    (item_id, user_id, value, datetime.now()))
        conn.commit()
        return print('Предмет добавлен в инвентарь')
    elif item_info:
        cur.execute("SELECT count FROM users_inventory WHERE owner_id = ? AND item_id = ?",
                    (user_id, item_id,))
        value += cur.fetchone()[0]
        cur.execute("UPDATE users_inventory SET count = ?, reg_time = ? WHERE owner_id = ? AND item_id = ?",
                    (value, datetime.now(), user_id, item_id,))
        conn.commit()
        return print('Предмет добавлен в инвентарь и стакнут')


def get_info_about_item(item_id):
    conn = sqlite3.connect('db/main.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM items WHERE item_id = ?", (item_id,))
    item = cur.fetchone()
    if item:
        return item
    else:
        return False


# Проверять наличие солдата в мейн коде, ну и при смерти удалять все предметы
def get_items(user_id):
    conn = sqlite3.connect('db/main.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users_inventory WHERE owner_id = ?", (user_id,))
    all_items = cur.fetchall()
    if all_items:
        return all_items
    else:
        return False


class Item:  # юзлес, т.к. вещи добавляются от руки в БД и от их лица ничего не происходит

    def __init__(self, info):
        self.item_id = info[0]
        self.name = info[1]
        self.type = info[2]
        self.desc = info[3]
        self.tier = info[4]

    def get_info(self):
        print(f'ID Предмета: {self.name}')
        print(f'Название: {self.name}')
        print(f'Тип предмета: {self.type}')
        print(f'Описание предмета: {self.desc}')
        print(f'Тир вещи: {self.tier}')


def main():
    pass


if __name__ == "__main__":
    main()
