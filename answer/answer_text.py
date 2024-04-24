# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий класс AnswerText."""

from aiogram.types import InlineKeyboardMarkup
from aiogram import types
from .answer import Answer, route_answer

class AnswerText(Answer):
    """! Класс-наблюдатель нажатия кнопки с шаблоном "Текст".
    """
    def __init__(self, manager_users) -> None:
        super().__init__(manager_users = manager_users)

    def create(self, cb_data: str, keyboard: list[list[InlineKeyboardMarkup]], text: str) -> None:
        """! Функция создает ответ бота по нажатию кнопки с шаблоном "Текст".

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
        async def answer_text(callback: types.CallbackQuery) -> None:
            check_user = self.manager_users.check_user(id_account = callback.from_user.id)
            if check_user == self.manager_users.state_user[0] or check_user == self.manager_users.state_user[1]:  
                formed_keyboard = InlineKeyboardMarkup (inline_keyboard = keyboard)
                await callback.message.answer(text = text, reply_markup = formed_keyboard)
                await callback.answer('')
            elif check_user == self.manager_users.state_user[3]:
                await callback.answer('Вы не зарегистрированы! Выполните команду /registration')
            elif check_user == self.manager_users.state_user[2]:
                await callback.answer('Вы в черном списке!')
