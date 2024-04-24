# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий класс InlineText."""

from .inline_menu import InlineMenu, route_inline_menu
from aiogram.types import InlineKeyboardMarkup, FSInputFile
from aiogram import types, F

class InlineText(InlineMenu):
    """! Класс-наблюдатель за сообщениями пользователя для вывода текста.
    """
    def __init__(self, manager_users: object) -> None:
        super().__init__(manager_users = manager_users)

    def create(self, name_menu: str, keyboard: list[list[InlineKeyboardMarkup]], 
               text: str, key_words: set) -> None:
        """! Функция создает наблюдателя за сообщениями пользователя. При совпадении ключевого слова или названия меню 
            с сообщением пользователя (в нижних регистрах) выводит картинку с текстом.
    
        @param name_menu - название меню.
        @param keyboard - список кнопок меню.
        @param text - текст.
        @param key_words - множество ключевых слов.

        Переменные:
            1. formed_keyboard - сформированное меню.
            2. check_user - результат проверки пользователя (False, True).
        
        Условие:
            1. Если пользователь в черном списке или не зарегистрирован вывод соответствующего сообщения.
        """
        @route_inline_menu.message(F.text.lower() == name_menu.lower())
        @route_inline_menu.message(F.text.lower().in_(key_words))
        async def create_inline_text_main(message: types.Message) -> None:
            check_user = self.manager_users.check_user(id_account = message.from_user.id)
            if check_user == self.manager_users.state_user[0] or check_user == self.manager_users.state_user[1]:   
                formed_keyboard = InlineKeyboardMarkup (inline_keyboard = keyboard)
                await message.answer(text = text, reply_markup = formed_keyboard)
            elif check_user == self.manager_users.state_user[3]:
                await message.answer('Вы не зарегистрированы! Выполните команду /registration')
            elif check_user== self.manager_users.state_user[2]:
                await message.answer('Вы в черном списке!')
            