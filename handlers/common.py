import logging
import json
from datetime import datetime
from aiogram import Dispatcher, types
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


async def cmd_start(message: types.Message):
    print(get_info_about_user(message))
    await message.reply(
        "Просто старт, не коксайз конечно но вот список команд /commands\n\nНовые прогнозы доступны черел пару часов")


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")
    dp.register_message_handler(cmd_list, commands='commands')
