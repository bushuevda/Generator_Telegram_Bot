# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий класс AnswerFile."""

from aiogram import types
from aiogram.types import FSInputFile, InlineKeyboardMarkup
from .answer import Answer, route_answer
from aiogram.exceptions import TelegramBadRequest

class AnswerFile(Answer):
    """! Класс-наблюдатель нажатия кнопки с шаблоном "Текст с файлом".
    """
    def __init__(self, manager_users: object) -> None:
        super().__init__(manager_users = manager_users)  

    def create(self, cb_data: str, file_path: str, 
               keyboard: list[list[InlineKeyboardMarkup]], caption: str) -> None:
        """! Функция создает ответ бота по нажатию кнопки с шаблоном "Текст с файлом".

        @param cb_data - текст для вызова события кнопки.
        @param file_path - путь к файлу.
        @param keyboard - список кнопок меню.
        @param caption - описание файла.

        Переменные:
            1. formed_file - подготовленный файл.
            2. formed_keyboard - сформированное меню.
            3. check_user - результат проверки пользователя (False, True).
        
        Условие:
            1. Если пользователь в черном списке или не зарегистрирован вывод соответствующего сообщения.
        """    
        @route_answer.callback_query(lambda c: c.data == cb_data)
        async def answer_file(callback: types.CallbackQuery) -> None:
            check_user = self.manager_users.check_user(id_account = callback.from_user.id)
            if check_user == self.manager_users.state_user[0] or check_user == self.manager_users.state_user[1]:   
                formed_file = FSInputFile(path = file_path)
                formed_keyboard = InlineKeyboardMarkup (inline_keyboard = keyboard)
                try:
                    await callback.message.answer_document(document = formed_file, reply_markup = formed_keyboard, caption = caption)
                    await callback.answer('')
                except TelegramBadRequest:
                    await callback.answer('')
            elif check_user == self.manager_users.state_user[3]:
                await callback.answer('Вы не зарегистрированы! Выполните команду /registration')
            elif check_user == self.manager_users.state_user[2]:
                await callback.answer('Вы в черном списке!')