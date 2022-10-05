from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import datetime
import asyncio


class CompetitionStage(StatesGroup):
    waiting_for_wallet = State()
    waiting_for_value = State()
    waiting_for_date = State()
    waiting_for_random = State()


