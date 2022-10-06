import logging
import json
from datetime import datetime
from aiogram import Dispatcher, types

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from modules.commands_list import CMD_LIST
from modules.buttons_list import start_kb, menu_kb


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


async def cmd_start(message: types.Message):
    print(get_info_about_user(message))
    await message.answer("Хеллоу, нажми кнопку 'Menu' чтобы посмотреть на доступные команды", reply_markup=start_kb)


async def cmd_menu(message: types.Message):
    print(get_info_about_user(message))
    await message.answer("*Меню управления игры*", reply_markup=menu_kb, parse_mode= 'Markdown')


async def cmd_cancel(message: types.Message):
    print(get_info_about_user(message))
    await message.reply("Клавиатура удалена", reply_markup=ReplyKeyboardRemove())


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")
    dp.register_message_handler(cmd_menu, text="Menu")
    dp.register_message_handler(cmd_cancel, commands="cancel")
    dp.register_message_handler(cmd_list, commands='commands')
