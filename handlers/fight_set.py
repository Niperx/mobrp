import asyncio
from datetime import datetime
import logging
from aiogram import Dispatcher, types
import random

from modules.buttons_list import *

import modules.soldier as soldier
import modules.inventory as inventory
import modules.quest as quest


def get_info_about_user(callback):
    text = f'\n##### {datetime.now()} #####\n'
    text += f'ID: {callback.from_user.id}, Text: {callback.data}'
    try:
        text += f'\nUsername: {callback.from_user.username},' \
                f' Name: {callback.from_user.first_name},' \
                f' Surname: {callback.from_user.last_name} '
    except Exception as e:
        logging.exception(e)
        text += 'Нет имени'
    return text


async def process_quests_btn_easy(callback_query: types.CallbackQuery):
    print(get_info_about_user(callback_query))
    info = f'*Задания  →  Тыл*'

    desc = f'\n\nЗадание: Подвоз провизии' \
           f'\nВремя выполнения 5 часов' \
           f'\nОпыт за задание: 20-35 ХР' \
           f'\nШанс успеха задания: 70%' \
           f'\nШанс дропа: 10% (50 проц)'

    text = info + desc
    # сделать передачу квеста в нижнию функцию так же как и с кнопками инвентаря, чтобы заранее видеть квест,
    # который подгружается (с помощью цифры в конце даты кнопки)
    await callback_query.message.edit_text(text, reply_markup=fight_kb, parse_mode='Markdown')


async def process_fight_btn(callback_query: types.CallbackQuery):
    print(get_info_about_user(callback_query))
    info = f'*Тыл  →  Выполнение...*'
    user_id = callback_query.from_user.id

    if soldier.check_state(user_id) == 'menu':  # проверка на свободное состояние
        # загрузка квеста и его параметров
        qw_num = random.randint(1, 2) # рандом изи квестов, добавить выбор сложности
        quest_info = quest.load_quest(qw_num)
        quest_succ = quest_info[5]
        stamina_request = quest_info[7]
        exp = [quest_info[4]-7, quest_info[4]+7]
        drop_chance = quest_info[6]
        mins_for_fight = quest_info[3]
        time_for_fight = mins_for_fight * 60  # время на выполнение задания
        demo_time = mins_for_fight * 60 // 400 # демо время
        print('Время файта', demo_time)
        user_info = soldier.load_soldier(user_id)
        sd = soldier.Soldier(user_info)
        if sd.stamina >= stamina_request:  # проверка на хватку стамины
            text = f'{info}\n\nВы на задании, время ожидания {mins_for_fight/60} часов/часа ({demo_time} сек)'
            await callback_query.message.edit_text(text, parse_mode='Markdown')

            soldier.set_state(user_id, 'fight')
            await asyncio.sleep(demo_time)
            succ = random.randint(1, 100)
            soldier_chance = sd.attack * 0.135 + sd.health * 0.324 + sd.mood * 0.270 + quest_succ
            if succ < soldier_chance:  # шанс на успех миссии
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
                # await callback_query.message.send_copy(-878891896, f'Пользователь @{callback_query.from_user.username} успешно закончил задание {quest_info[2]}')
            else:  # шанс на луз
                print(f'Какой выпал шанс {succ}')
                print(f'Какие у меня шансы {soldier_chance}')
                text = f'{info}\nВы сражались за Родину как герой, Народ вас не забудет'
                soldier.delete_soldier(user_id)
                await callback_query.message.edit_text(text, reply_markup=soldier_kb, parse_mode='Markdown')
                # await callback_query.message.send_copy(-878891896,
                #                                        f'Пользователь @{callback_query.from_user.username} погиб на задании {quest_info[2]}')

            soldier.set_state(user_id, 'menu')

        else:
            text = f'{info}\nНедостаточно стамины, {sd.stamina} из {stamina_request}'
            await callback_query.message.edit_text(text, reply_markup=soldier_kb, parse_mode='Markdown')

    else:
        text = f'{info}\nВаш солдат на текущий момент уже занят'
        await callback_query.message.edit_text(text, reply_markup=soldier_kb, parse_mode='Markdown')


def register_handlers_fight_set(dp: Dispatcher):
    # Кнопки состояния "Отдых"
    dp.register_callback_query_handler(process_quests_btn_easy, lambda c: c.data == 'quests_btn_easy')
    dp.register_callback_query_handler(process_fight_btn, lambda c: c.data == 'fight_btn')

