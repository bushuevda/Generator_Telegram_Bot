# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий абстрактный класс InlineMenu."""

from aiogram.types import InlineKeyboardButton
from aiogram import Router

route_inline_menu = Router()

class InlineMenu:
    """! Абстрактный класс наблюдатель за сообщениями пользователя.
    """
    def __init__(self, manager_users) -> None:
        ## Класс-менеджер пользователей.
        self.manager_users = manager_users

