import logging
import asyncio
from datetime import datetime
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from modules.buttons_list import *
import modules.soldier as soldier
import modules.inventory as inventory


class CompetitionStage(StatesGroup):
    waiting_for_name = State()


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


async def process_btn_menu(callback_query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    x = "*Меню управления игры*"
    await callback_query.message.edit_text(x, reply_markup=menu_kb, parse_mode='Markdown')


async def process_menu_btn1(callback_query: types.CallbackQuery):
    info = callback_query.message.reply_markup.inline_keyboard[0][0].text
    info = f'*{callback_query.message.text}  →  {info}*'
    user_id = callback_query.from_user.id
    cnt = soldier.check_count(user_id)
    if cnt == 0:
        text = f'{info}\n\nСолдат отсутствует, погодите пару секунд, мобилизируем для вас одного\n\nДайте ему новое *ИМЯ*:\n_(Напишите в сообщении)_'
        await callback_query.message.edit_text(text, reply_markup=soldier_kb, parse_mode='Markdown')
        await CompetitionStage.waiting_for_name.set()
    else:
        user_info = soldier.load_soldier(user_id)
        sd = soldier.Soldier(user_info)
        text = f'{info}\n\n*Имя:* {sd.name.title()}\n*Здоровье:* {sd.health} | *Атака:* {sd.attack}'
        text += f'\n*Настрой:* {sd.mood}\n*Выносливость:* {sd.stamina}\n*Звание:* {soldier.get_rank(sd.exp).title()}'
        await callback_query.message.edit_text(text, reply_markup=soldier_kb, parse_mode='Markdown')


async def process_soldier_get_name(message: types.Message, state: FSMContext):
    name = message.text.lower()  # Можно сделать функцию обработчик валидности ника
    await state.finish()
    soldier.create_soldier(message.from_user.id, name)
    await message.answer("*Меню управления игры*", reply_markup=menu_kb, parse_mode='Markdown')


async def process_menu_btn2(callback_query: types.CallbackQuery):
    info = callback_query.message.reply_markup.inline_keyboard[0][1].text
    info = f'*{callback_query.message.text}  →  {info}*'

    user_id = callback_query.from_user.id
    cnt = soldier.check_count(user_id)
    if cnt:
        text = f'{info}\n\n_(Описание заданий)_'
        await callback_query.message.edit_text(text, reply_markup=quests_kb, parse_mode='Markdown')
    else:
        text = f'{info}\n\nУ вас отсутствует нанятый солдат, перейдите во вкладку *Призывники* в главном меню'
        await callback_query.message.edit_text(text, reply_markup=soldier_kb, parse_mode='Markdown')


async def process_menu_btn3(callback_query: types.CallbackQuery):
    info = callback_query.message.reply_markup.inline_keyboard[1][0].text
    info = f'*{callback_query.message.text}  →  {info}*'

    user_id = callback_query.from_user.id
    cnt = soldier.check_count(user_id)
    if cnt:
        items = inventory.get_items(user_id)
        inv_kb = InlineKeyboardMarkup()
        if items:
            for item in items:
                item_info = inventory.get_info_about_item(item[0])
                button_name = f'{item_info[1]} || {item[2]} шт.'
                button = InlineKeyboardButton(button_name, callback_data=f'inv_info_btn_{item[0]}')
                inv_kb.insert(button)
            inv_kb.row(quests_btn_menu)
            await callback_query.message.edit_text(info, reply_markup=inv_kb, parse_mode='Markdown')
        else:
            text = f'{info}\n\n_(пусто)_'
            await callback_query.message.edit_text(text, reply_markup=soldier_kb, parse_mode='Markdown')
    else:
        text = f'{info}\n\nУ вас отсутствует нанятый солдат, перейдите во вкладку *Призывники* в главном меню'
        await callback_query.message.edit_text(text, reply_markup=soldier_kb, parse_mode='Markdown')


async def process_inv_info_btn(callback_query: types.CallbackQuery):
    info = f'*{callback_query.message.text}*'
    data = callback_query.data
    item = int(data[data.rfind('_') + 1:])
    item_info = inventory.get_info_about_item(item)
    await callback_query.message.edit_text(
        f'{info}\n\n*Название:* {item_info[1].title()}\n*Тип:* {item_info[2].title()}\n*Описание:* {item_info[3]}',
        reply_markup=soldier_kb, parse_mode='Markdown')


async def process_menu_btn4(callback_query: types.CallbackQuery):
    info = callback_query.message.reply_markup.inline_keyboard[1][1].text
    info = f'*{callback_query.message.text} → {info}*\nОтдых будет составлять 3 часа, уверены?'
    await callback_query.message.edit_text(info, reply_markup=chill_kb, parse_mode='Markdown')


def register_handlers_menu_controller(dp: Dispatcher):
    dp.register_message_handler(process_soldier_get_name, state=CompetitionStage.waiting_for_name)
    dp.register_callback_query_handler(process_btn_menu, lambda c: c.data == 'btn_menu', state='*')
    dp.register_callback_query_handler(process_menu_btn1, lambda c: c.data == 'menu_btn1')
    dp.register_callback_query_handler(process_menu_btn2, lambda c: c.data == 'menu_btn2')
    dp.register_callback_query_handler(process_menu_btn3, lambda c: c.data == 'menu_btn3')
    dp.register_callback_query_handler(process_menu_btn4, lambda c: c.data == 'menu_btn4')
    dp.register_callback_query_handler(process_inv_info_btn, lambda c: 'inv_info_btn' in c.data)
