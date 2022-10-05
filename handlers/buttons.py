import logging
import json
from datetime import datetime
from aiogram import Dispatcher, types

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from modules.commands_list import CMD_LIST


def get_info_about_user(message):
    text = f'\n##### {datetime.now()} #####\n'
    text += f'ID: {message.from_user.id}, Text: {message.text}'
    try:
        text += f'\nUsername: {message.from_user.username},' \
                f' Name: {message.from_user.first_name},' \
                f' Surname: {message.from_user.last_name} '
    except Exception as e:
        logging.exception(e)
        text += 'Нет имени'
    return text


async def cmd_list(message: types.Message):
    print(get_info_about_user(message))
    text = 'Список команд:\n\n'
    for cmd in CMD_LIST:
        text += f'{cmd[0]} - {cmd[1]}\n'
    await message.answer(text)


# async def cmd_start(message: types.Message):
#     print(get_info_about_user(message))
#     await message.reply(
#         "Просто старт, не коксайз конечно но вот список команд /commands\n\nНовые прогнозы доступны черел пару часов")


menu_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Menu'))

start_btn1 = InlineKeyboardButton('Призывник', callback_data='start_btn1')
start_btn2 = InlineKeyboardButton('Задания', callback_data='start_btn2')
start_btn3 = InlineKeyboardButton('Инвентарь', callback_data='start_btn3')
start_btn4 = InlineKeyboardButton('Отдых', callback_data='start_btn4')
start_kb = InlineKeyboardMarkup()
start_kb.row(start_btn1, start_btn2)
start_kb.row(start_btn3, start_btn4)

soldier_btn1 = InlineKeyboardButton('Основные хар-ки', callback_data='soldier_btn1')
soldier_btn2 = InlineKeyboardButton('Выносливость', callback_data='soldier_btn2')
soldier_btn3 = InlineKeyboardButton('Звание', callback_data='soldier_btn3')
soldier_btn_menu = InlineKeyboardButton('Меню', callback_data='btn_menu')
soldier_kb = InlineKeyboardMarkup()
soldier_kb.row(soldier_btn1)
soldier_kb.row(soldier_btn2)
soldier_kb.row(soldier_btn3)
soldier_kb.row(soldier_btn_menu)

quests_btn1 = InlineKeyboardButton('Задание 1', callback_data='quests_btn1')
quests_btn2 = InlineKeyboardButton('Задание 2', callback_data='quests_btn2')
quests_btn3 = InlineKeyboardButton('Задание 3', callback_data='quests_btn3')
quests_btn4 = InlineKeyboardButton('Задание 4', callback_data='quests_btn4')
quests_btn_menu = InlineKeyboardButton('Меню', callback_data='btn_menu')
quests_kb = InlineKeyboardMarkup()
quests_kb.row(quests_btn1, quests_btn2)
quests_kb.row(quests_btn3, quests_btn4)
quests_kb.row(quests_btn_menu)


async def cmd_start(message: types.Message):
    print(get_info_about_user(message))
    await message.answer("Хеллоу, нажми кнопку 'Menu' чтобы посмотреть на доступные команды", reply_markup=menu_kb)


async def cmd_menu(message: types.Message):
    print(get_info_about_user(message))
    await message.answer("Меню управления игры:", reply_markup=start_kb)


async def cmd_cancel(message: types.Message):
    print(get_info_about_user(message))
    await message.reply("Клавиатура удалена", reply_markup=ReplyKeyboardRemove())


async def process_btn_menu(callback_query: types.CallbackQuery):  # сделать считывание текста кнопки и встраивание в edit.text
    await callback_query.message.edit_text("Меню управления игры:", reply_markup=start_kb)


async def process_btn1(callback_query: types.CallbackQuery):  # сделать считывание текста кнопки и встраивание в edit.text
    x = 'Призывник:'
    print(callback_query)
    await callback_query.message.edit_text(x, reply_markup=soldier_kb)


async def process_btn2(callback_query: types.CallbackQuery):  # сделать считывание текста кнопки и встраивание в edit.text
    x = 'Задания:'
    await callback_query.message.edit_text(x, reply_markup=soldier_kb)


async def process_btn3(callback_query: types.CallbackQuery):  # сделать считывание текста кнопки и встраивание в edit.text
    x = 'Инвентарь:'
    await callback_query.message.edit_text(x, reply_markup=soldier_kb)


async def process_btn4(callback_query: types.CallbackQuery):  # сделать считывание текста кнопки и встраивание в edit.text
    await callback_query.message.answer('Ушёл на отдых')


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")
    dp.register_message_handler(cmd_menu, text="Menu")
    dp.register_message_handler(cmd_cancel, commands="cancel")
    dp.register_message_handler(cmd_list, commands='commands')

    dp.register_callback_query_handler(lambda c: c.data == 'bt1', process_btn1)
