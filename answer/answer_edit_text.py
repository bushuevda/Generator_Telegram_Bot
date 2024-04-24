# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий класс AnswerEditText."""

from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from .answer import Answer, route_answer

class AnswerEditText(Answer):
    """! Класс-наблюдатель нажатия кнопки для изменения текста.
    """
    def __init__(self, manager_users: object) -> None:
        super().__init__(manager_users = manager_users)

    def create(self, cb_data: str, keyboard: list[list[InlineKeyboardMarkup]], text: str) -> None:
        """! Функция создает наблюдателя за нажатием клавиши с шаблоном "Изменение текста".
        
        @param cb_data - текст для вызова события кнопки.
        @param keyboard - список кнопок меню.
        @param text - текст.

        Переменные:
            1. formed_image - подготовленное изображение.
            2. formed_keyboard - сформированное меню.
            3. check_user - результат проверки пользователя (False, True).
        
        Условие:
            1. Если пользователь в черном списке или не зарегистрирован вывод соответствующего сообщения.
        """   
        @route_answer.callback_query(lambda c: c.data == cb_data)
        async def answer_edit_text(callback: types.CallbackQuery) -> None:
            check_user = self.manager_users.check_user(id_account = callback.from_user.id)
            if check_user == self.manager_users.state_user[0] or check_user == self.manager_users.state_user[1]:  
                formed_keyboard = InlineKeyboardMarkup (inline_keyboard = keyboard)
                await callback.message.edit_text(text = text, reply_markup = formed_keyboard)
                await callback.answer('')
            elif check_user == self.manager_users.state_user[3]:
                await callback.answer('Вы не зарегистрированы! Выполните команду /registration')
            elif check_user == self.manager_users.state_user[2]:
                await callback.answer('Вы в черном списке!')