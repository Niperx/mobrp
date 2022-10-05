import logging
from datetime import datetime
from aiogram import Dispatcher, types

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from modules.buttons_list import *


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


async def cmd_menu(message: types.Message):
    print(get_info_about_user(message))
    await message.answer("Меню управления игры:", reply_markup=soldier_kb)


async def process_btn_menu(callback_query: types.CallbackQuery):  # сделать считывание текста кнопки и встраивание в edit.text
    x = "Меню управления игры:"
    await callback_query.message.edit_text(x, reply_markup=menu_kb)


async def process_menu_btn1(callback_query: types.CallbackQuery):  # сделать считывание текста кнопки и встраивание в edit.text
    x = 'Призывник:'
    await callback_query.message.edit_text(x, reply_markup=soldier_kb)


async def process_menu_btn2(callback_query: types.CallbackQuery):  # сделать считывание текста кнопки и встраивание в edit.text
    x = 'Задания:'
    await callback_query.message.edit_text(x, reply_markup=quests_kb)


async def process_menu_btn3(callback_query: types.CallbackQuery):  # сделать считывание текста кнопки и встраивание в edit.text
    x = 'Инвентарь:'
    await callback_query.message.edit_text(x, reply_markup=inv_kb)


async def process_menu_btn4(callback_query: types.CallbackQuery):  # сделать считывание текста кнопки и встраивание в edit.text
    await callback_query.message.edit_text('Ушёл на отдых')


def register_handlers_menu_controller(dp: Dispatcher):
    dp.register_message_handler(cmd_menu, text="Menu")
    # dp.register_callback_query_handler(lambda c: c.data == 'btn_menu', process_btn_menu)
    dp.register_callback_query_handler('menu_btn1', process_menu_btn1)

    dp.register_callback_query_handler(lambda c: c.data == 'menu_btn2', process_menu_btn2)
    dp.register_callback_query_handler(lambda c: c.data == 'menu_btn3', process_menu_btn3)
    dp.register_callback_query_handler(lambda c: c.data == 'menu_btn4', process_menu_btn4)
