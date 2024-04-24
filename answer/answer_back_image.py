# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий класс AnswerBackImage."""

from aiogram.types import FSInputFile, InlineKeyboardMarkup, InputMediaPhoto
from aiogram import types, Bot
from .answer import Answer, route_answer
from aiogram.exceptions import TelegramBadRequest

class AnswerBackImage(Answer):
    """! Класс-наблюдатель нажатия кнопки назад для смены изображения.
    """
    def __init__(self, manager_users: object) -> None:
        super().__init__(manager_users = manager_users)

    def create(self, cb_data: str, path_images: list[str],
                       keyboard: list[list[InlineKeyboardMarkup]], captions: list[str]) -> None:
        """! Функция создает наблюдателя за нажатием клавиши назад для переключения изображения.

        @param cb_data - текст для вызова события кнопки.
        @param path_images - список путей к изображениям.
        @param keyboard - список кнопок меню.
        @param captions - список описаний изображений.

        Переменные:
            1. formed_image - подготовленное изображение.
            2. formed_keyboard - сформированное меню.
            3. check_user - результат проверки пользователя (False, True).
        
        Условия:
            1. Если количество изображений больше self.count_image -> self.count_image ++ (инкермент).
            2. Если количество изображений равно self.count_image -> self.count_image = 0 (обнуление).
            3. Если пользователь в черном списке или не зарегистрирован вывод соответствующего сообщения.
        """
        @route_answer.callback_query(lambda c: c.data == cb_data)
        async def answer_back_image(callback: types.CallbackQuery, bot:Bot) -> None:
            check_user = self.manager_users.check_user(id_account = callback.from_user.id)
            if check_user == self.manager_users.state_user[0] or check_user == self.manager_users.state_user[1]:            
                if(len(path_images) > self.count_image):
                    self.count_image += 1
                if self.count_image == len(path_images):
                    self.count_image = 0
                formed_images = FSInputFile(path_images[self.count_image])
                formed_keyboard = InlineKeyboardMarkup (inline_keyboard = keyboard)
                try:
                    await bot.edit_message_media(chat_id=callback.message.chat.id,message_id = callback.message.message_id,
                                                media=InputMediaPhoto(media = formed_images, caption = captions[self.count_image]),
                                                reply_markup = formed_keyboard)
                except:
                    await callback.answer('')
            elif check_user == self.manager_users.state_user[3]:
                await callback.answer('Вы не зарегистрированы! Выполните команду /registration')
            elif check_user == self.manager_users.state_user[2]:
                await callback.answer('Вы в черном списке!')