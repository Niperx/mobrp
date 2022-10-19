import asyncio
from aiogram import Dispatcher, types
import random

from modules.buttons_list import *

import modules.soldier as soldier
import modules.inventory as inventory


async def process_quests_btn_easy(callback_query: types.CallbackQuery):
    info = f'*Задания  →  Тыл*'

    desc = f'\n\nЗадание: Подвоз провизии' \
           f'\nВремя выполнения 5 часов' \
           f'\nОпыт за задание: 20-35 ХР' \
           f'\nШанс успеха задания: 70%' \
           f'\nШанс дропа: 10% (50 проц)'

    text = info + desc
    await callback_query.message.edit_text(text, reply_markup=fight_kb, parse_mode='Markdown')


async def process_fight_btn(callback_query: types.CallbackQuery):
    info = f'*Тыл  →  Выполнение...*'
    user_id = callback_query.from_user.id

    text = f'{info}\n\nВы на задании, время ожидания 5 часов (30 сек)'
    await callback_query.message.edit_text(text, parse_mode='Markdown')

    await asyncio.sleep(1)

    quest_succ = 70
    stamina_request = 15
    exp = [20, 35]
    drop_chance = 50
    user_info = soldier.load_soldier(user_id)
    sd = soldier.Soldier(user_info)
    if sd.stamina >= stamina_request:  # проверка на хватку стамины
        succ = random.randint(1, 100)
        soldier_chance = sd.attack * 0.135 + sd.health * 0.324 + sd.mood * 0.270 + quest_succ
        if succ < soldier_chance:  # шанс на успех
            print(f'Какой выпал шанс {succ}')
            print(f'Какие у меня шансы {soldier_chance}')
            # добавляем статы
            rnd_exp = random.randint(exp[0], exp[1])
            sd.exp += rnd_exp
            sd.stamina -= 15
            sd.mood -= random.randint(-10, 10)
            sd.upload_info()
            # добавляем предметы
            item_chance = random.randint(1, 100)
            print(f'\n\nКакой выпал шанс предмета {item_chance}')
            print(f'Какие у меня шансы {drop_chance}')
            if item_chance < drop_chance:  # шанс на дроп
                rnd_item = random.randint(1, 5)
                rnd_item_info = inventory.get_info_about_item(rnd_item)
                inventory.add_items(user_id, rnd_item, value=1)
                text = f'{info}\n\nПоздравляем с успешным выполнением задания,\n\n*Ваши награды:*\nОпыт: {rnd_exp}\n\n*Предметы:*\n{rnd_item_info[1]}'
            else:
                text = f'{info}\n\nПоздравляем с успешным выполнением задания,\n\n*Ваши награды:*\nОпыт: {rnd_exp}'

            await callback_query.message.edit_text(text, reply_markup=soldier_kb, parse_mode='Markdown')
        else:  # шанс на луз
            print(f'Какой выпал шанс {succ}')
            print(f'Какие у меня шансы {soldier_chance}')
            text = f'{info}\nВы сражались за Родину как герой, Народ вас не забудет'
            soldier.delete_soldier(user_id)
            await callback_query.message.edit_text(text, reply_markup=soldier_kb, parse_mode='Markdown')

    else:
        text = f'{info}\nНедостаточно стамины, {sd.stamina} из {stamina_request}'
        await callback_query.message.edit_text(text, reply_markup=soldier_kb, parse_mode='Markdown')


def register_handlers_fight_set(dp: Dispatcher):
    # Кнопки состояния "Отдых"
    dp.register_callback_query_handler(process_quests_btn_easy, lambda c: c.data == 'quests_btn_easy')
    dp.register_callback_query_handler(process_fight_btn, lambda c: c.data == 'fight_btn')

