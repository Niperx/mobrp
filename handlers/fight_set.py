import asyncio
from aiogram import Dispatcher, types

from modules.buttons_list import *

import modules.soldier as soldier
import modules.inventory as inventory


async def process_quests_btn_easy(callback_query: types.CallbackQuery):
    info = f'*Задания  →  Тыл*'

    desc = f'\n\nЗадание: Подвоз провизии' \
           f'\nВремя выполнения 5 часов' \
           f'\nОпыт за задание: 20-35 ХР' \
           f'\nШанс успеха задания: 70%' \
           f'\nШанс дропа: 10%'

    text = info + desc
    await callback_query.message.edit_text(text, reply_markup=fight_kb, parse_mode='Markdown')


async def process_fight_btn(callback_query: types.CallbackQuery):
    info = f'*Тыл  →  Выполнение...*'


def register_handlers_fight_set(dp: Dispatcher):
    # Кнопки состояния "Отдых"
    dp.register_callback_query_handler(process_quests_btn_easy, lambda c: c.data == 'quests_btn_easy', state=MenuStage.menu)

