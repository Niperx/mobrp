from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


class MenuStage(StatesGroup):
    menu = State()
    waiting_for_name = State()
    chill = State()
    fight = State()


# Клавиатура обычная с кнопкой "Меню"
start_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Menu'))

# Клавиатура освного меню
menu_btn1 = InlineKeyboardButton('Призывник', callback_data='menu_btn1')
menu_btn2 = InlineKeyboardButton('Задания', callback_data='menu_btn2')
menu_btn3 = InlineKeyboardButton('Инвентарь', callback_data='menu_btn3')
menu_btn4 = InlineKeyboardButton('Отдых', callback_data='menu_btn4')
menu_kb = InlineKeyboardMarkup()
menu_kb.row(menu_btn1, menu_btn3)
menu_kb.row(menu_btn2)
menu_kb.row(menu_btn4)

# Клавиатура призывника (есть)
soldier_btn_menu = InlineKeyboardButton('Меню', callback_data='btn_menu')
soldier_kb = InlineKeyboardMarkup()
soldier_kb.row(soldier_btn_menu)

# Клавиатура заданий
quests_btn1 = InlineKeyboardButton('Тыл', callback_data='quests_btn_easy')
quests_btn2 = InlineKeyboardButton('Наступление', callback_data='quests_btn_medium')
quests_btn3 = InlineKeyboardButton('Диверсия', callback_data='quests_btn_hard')
quests_btn_menu = InlineKeyboardButton('Меню', callback_data='btn_menu')
quests_kb = InlineKeyboardMarkup()
quests_kb.row(quests_btn1, quests_btn2, quests_btn3)
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
chill_btn = InlineKeyboardButton('Отдохнуть', callback_data='chill_btn1')
chill_btn_menu = InlineKeyboardButton('Меню', callback_data='btn_menu')
chill_kb = InlineKeyboardMarkup()
chill_kb.row(chill_btn, chill_btn_menu)

# Клавиатура в бой
fight_btn = InlineKeyboardButton('В бой', callback_data='fight_btn')
fight_btn_menu = InlineKeyboardButton('Меню', callback_data='btn_menu')
fight_kb = InlineKeyboardMarkup()
fight_kb.row(fight_btn, fight_btn_menu)
