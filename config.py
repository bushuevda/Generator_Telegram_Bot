# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий настройки."""

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from inline_menu import route_inline_menu
from reply_menu import router_reply_menu
from answer import route_answer
import random
import json

with open("setting.json", "r", encoding = 'utf8') as read_file:
    data = dict(json.load(read_file))

NAME_DB = data['settings']['NAME_DB']
BOT_TOKEN = data['settings']['BOT_TOKEN']
WELCOME_MESSAGE = data['settings']['WELCOME_MESSAGE']
if data['settings']['PASSWORD_REGISTRATION']:
    password_registration = data['settings']['PASSWORD_REGISTRATION']
else:
    password_registration = str(random.randint(10, 1000000000))
print("Пароль для регистрации пользователя: ", password_registration)
dp: Dispatcher = Dispatcher(storage = MemoryStorage())
dp.include_router(route_inline_menu)
dp.include_router(router_reply_menu)
dp.include_router(route_answer)

        
