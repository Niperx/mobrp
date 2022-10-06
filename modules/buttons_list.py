from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# Клавиатура обычная с кнопкой "Меню"
start_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Menu'))

# Клавиатура освного меню
menu_btn1 = InlineKeyboardButton('Призывник', callback_data='menu_btn1')
menu_btn2 = InlineKeyboardButton('Задания', callback_data='menu_btn2')
menu_btn3 = InlineKeyboardButton('Инвентарь', callback_data='menu_btn3')
menu_btn4 = InlineKeyboardButton('Отдых', callback_data='menu_btn4')
menu_kb = InlineKeyboardMarkup()
menu_kb.row(menu_btn1, menu_btn2)
menu_kb.row(menu_btn3, menu_btn4)

# Клавиатура призывника
soldier_btn_menu = InlineKeyboardButton('Меню', callback_data='btn_menu')
soldier_kb = InlineKeyboardMarkup()
soldier_kb.row(soldier_btn_menu)

# Клавиатура заданий
quests_btn1 = InlineKeyboardButton('Задание 1', callback_data='quests_btn1')
quests_btn2 = InlineKeyboardButton('Задание 2', callback_data='quests_btn2')
quests_btn3 = InlineKeyboardButton('Задание 3', callback_data='quests_btn3')
quests_btn4 = InlineKeyboardButton('Задание 4', callback_data='quests_btn4')
quests_btn_menu = InlineKeyboardButton('Меню', callback_data='btn_menu')
quests_kb = InlineKeyboardMarkup()
quests_kb.row(quests_btn1, quests_btn2)
quests_kb.row(quests_btn3, quests_btn4)
quests_kb.row(quests_btn_menu)

# Клавиатура инвентаря
inv_btn1 = InlineKeyboardButton('Предмет 1', callback_data='inv_btn1')
inv_btn2 = InlineKeyboardButton('Предмет 2', callback_data='inv_btn2')
inv_btn3 = InlineKeyboardButton('Предмет 3', callback_data='inv_btn3')
inv_btn4 = InlineKeyboardButton('Предмет 4', callback_data='inv_btn4')
inv_btn_menu = InlineKeyboardButton('Меню', callback_data='btn_menu')
inv_kb = InlineKeyboardMarkup()
inv_kb.row(inv_btn1, inv_btn2)
inv_kb.row(inv_btn3, inv_btn4)
inv_kb.row(inv_btn_menu)

# Клавиатура отдыха
chill_btn1 = InlineKeyboardButton('Да', callback_data='chill_btn1')
chill_btn_menu = InlineKeyboardButton('Назад в меню', callback_data='btn_menu')
chill_kb = InlineKeyboardMarkup()
chill_kb.row(chill_btn1, chill_btn_menu)