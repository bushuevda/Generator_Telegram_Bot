# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий класс InlineFile."""

from .inline_menu import InlineMenu, route_inline_menu
from aiogram.types import InlineKeyboardMarkup, FSInputFile
from aiogram import types,  F

class InlineFile(InlineMenu):
    """! Класс-наблюдатель за сообщениями пользователя для вывода файла с текстом.
    """
    def __init__(self, manager_users) -> None:
        super().__init__(manager_users = manager_users)

    def create(self, name_menu: str, key_words: set, file_path: str, 
               keyboard: list[list[InlineKeyboardMarkup]], caption: str) -> None:

        """! Функция создает наблюдателя за сообщениями пользователя. При совпадении ключевого слова или названия меню 
            с сообщением пользователя (в нижних регистрах) выводит файл с текстом.
        
        @param name_menu - название меню.
        @param key_words - множество ключевых слов.
        @param file_path - путь к файлу.
        @param keyboard -  список кнопок меню.
        @param caption -  описание файла.

        Переменные:
            1. formed_file - подготовленный файл.
            2. formed_keyboard - сформированное меню.
            3. check_user - результат проверки пользователя (False, True).
        
        Условие:
            1. Если пользователь в черном списке или не зарегистрирован вывод соответствующего сообщения.
        """
        @route_inline_menu.message(F.text.lower() == name_menu.lower())
        @route_inline_menu.message(F.text.lower().in_(key_words))
        async def create_inline_file(message: types.Message) -> None:
            check_user = self.manager_users.check_user(id_account = message.from_user.id)
            if check_user == self.manager_users.state_user[0] or check_user == self.manager_users.state_user[1]:  
                formed_file = FSInputFile(path = file_path)
                formed_keyboard = InlineKeyboardMarkup(inline_keyboard = keyboard)
                await message.reply_document(document = formed_file, reply_markup = formed_keyboard, caption = caption)
            elif check_user == self.manager_users.state_user[3]:
                await message.answer('Вы не зарегистрированы! Выполните команду /registration')
            elif check_user == self.manager_users.state_user[2]:
                await message.answer('Вы в черном списке!')
            