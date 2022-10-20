import sqlite3


def load_quest(quest_id):
    conn = sqlite3.connect('db/main.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM quests WHERE quest_id = ?", (quest_id,))
    info = cur.fetchone()
    return info


def main():
    x = load_quest(1)
    print(x)


if __name__ == "__main__":
    main()
