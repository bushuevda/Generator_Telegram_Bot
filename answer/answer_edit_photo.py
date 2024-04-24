# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий класс AnswerEditPhoto."""

from aiogram import Bot
from aiogram import types
from aiogram.types import FSInputFile, InlineKeyboardMarkup
from .answer import Answer, route_answer

class AnswerEditPhoto(Answer):
    """! Класс-наблюдатель нажатия кнопки для изменения текста с картинкой.
    """
    def __init__(self, manager_users: object) -> None:
        super().__init__(manager_users = manager_users)

    def create(self, cb_data: str, list_path_image: list[str],
                       keyboard: list[list[InlineKeyboardMarkup]], list_caption: list[str]) -> None:
        """! Функция создает наблюдателя за нажатием клавиши с шаблоном "Изменение текста с картинкой".

        @param cb_data - текст для вызова события кнопки.
        @param list_path_image - список путей к изображениям.
        @param keyboard - список кнопок меню.
        @param list_caption - список описаний изображений.

        Переменные:
            1. formed_image - подготовленное изображение.
            2. formed_keyboard - сформированное меню.
            3. check_user - результат проверки пользователя (False, True).
        
        Условие:
            1. Если пользователь в черном списке или не зарегистрирован вывод соответствующего сообщения.
        """       
        @route_answer.callback_query(lambda c: c.data == cb_data)
        async def answer_edit_photo(callback: types.CallbackQuery) -> None:
            check_user = self.manager_users.check_user(id_account = callback.from_user.id)
            if check_user == self.manager_users.state_user[0] or check_user == self.manager_users.state_user[1]:  
                formed_image = FSInputFile(list_path_image[self.count_image])
                formed_keyboard = InlineKeyboardMarkup (inline_keyboard = keyboard)
                await callback.message.answer_photo(photo = formed_image, reply_markup = formed_keyboard,
                                                    caption = list_caption[self.count_image])
                await callback.answer('')
            elif check_user == self.manager_users.state_user[3]:
                await callback.answer('Вы не зарегистрированы! Выполните команду /registration')
            elif check_user == self.manager_users.state_user[2]:
                await callback.answer('Вы в черном списке!')