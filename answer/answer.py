# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий абстрактный класс Answer."""

from aiogram.types import InlineKeyboardButton
from aiogram import Router

route_answer = Router()

class Answer:
    """! Абстрактный класс-наблюдатель
    """
    def __init__(self, manager_users) -> None:
        ## Переменная счетчик переключаемых изображений.
        self.count_image = int(0)
        ## Класс-менеджер пользователей.
        self.manager_users = manager_users
