import logging
import random
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


async def process_btn_menu(callback_query: types.CallbackQuery):
    x = "*Меню управления игры*"
    await callback_query.message.edit_text(x, reply_markup=menu_kb, parse_mode= 'Markdown')

zv = ['Рядовой', 'Ефрейтор', 'Мл. Сержант', 'Сержант', 'Ст. Сержант', 'Старшина', 'Прапорщик', 'Ст. Прапорщи']
async def process_menu_btn1(callback_query: types.CallbackQuery):
    info = callback_query.message.reply_markup.inline_keyboard[0][0].text
    info = f'*{callback_query.message.text}  →  {info}*'
    health, attack, mood, stamina = 50, 20, 50, 0
    info += f'\n*Здоровье:* {health}\n*Атака:* {attack}\n*Настрой:* {mood}'
    info += f'\n*Выносливость:* {stamina}\n*Звание:* {random.choice(zv)}'
    await callback_query.message.edit_text(info, reply_markup=soldier_kb, parse_mode='Markdown')


async def process_menu_btn2(callback_query: types.CallbackQuery):
    info = callback_query.message.reply_markup.inline_keyboard[0][0].text
    info = f'*{callback_query.message.text}  →  {info}*'
    await callback_query.message.edit_text(info, reply_markup=quests_kb, parse_mode= 'Markdown')


async def process_menu_btn3(callback_query: types.CallbackQuery):
    info = callback_query.message.reply_markup.inline_keyboard[0][0].text
    info = f'*{callback_query.message.text}  →  {info}*'
    await callback_query.message.edit_text(info, reply_markup=inv_kb, parse_mode= 'Markdown')


async def process_menu_btn4(callback_query: types.CallbackQuery):
    info = callback_query.message.reply_markup.inline_keyboard[0][0].text
    info = f'*{callback_query.message.text} → {info}*\nОтдых будет составлять N часов, уверены?'
    await callback_query.message.edit_text(info, reply_markup=chill_kb, parse_mode= 'Markdown')


def register_handlers_menu_controller(dp: Dispatcher):
    dp.register_callback_query_handler(process_btn_menu, lambda c: c.data == 'btn_menu')
    dp.register_callback_query_handler(process_menu_btn1, lambda c: c.data == 'menu_btn1')
    dp.register_callback_query_handler(process_menu_btn2, lambda c: c.data == 'menu_btn2')
    dp.register_callback_query_handler(process_menu_btn3, lambda c: c.data == 'menu_btn3')
    dp.register_callback_query_handler(process_menu_btn4, lambda c: c.data == 'menu_btn4')
