# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий класс InlineAnecdote."""

from .inline_menu import InlineMenu, route_inline_menu
from aiogram.types import InlineKeyboardMarkup, FSInputFile
from aiogram import types, F
from aiogram.filters.command import Command
import random

class InlineAnecdote(InlineMenu):
    """! Класс-наблюдатель за сообщениями пользователя для вывода анекдота.
    """
    def __init__(self, manager_users: object, len_list_anecdotes: int) -> None:
        super().__init__(manager_users = manager_users)
        ## Количество анекдотов в базе данных
        self.len_list_anecdotes = len_list_anecdotes

    def create(self, get_anecdote: object) -> None:
        """! Функция создает наблюдателя за сообщениями пользователя. При совпадении ключевого слова или названия меню 
            с сообщением пользователя (в нижних регистрах) выводит анекдот.
    
        @param get_anecdote - функция получения анекдота по id анекдота.

        Переменные:
            1. get_text - текст анекдота полученного с помощью функции get_anecdote.
            1. id_anecdote - случайное число в диапазоне от 1 до количества анекдотов в базе данных.
            3. command_text - текст с командой вывода еще одного анекдота.
            4. text - конкатенация get_text и command_text.
            5. check_user - результат проверки пользователя (False, True).
        
        Условие:
            1. Если пользователь в черном списке или не зарегистрирован вывод соответствующего сообщения.
        """
        @route_inline_menu.message(Command("anecdote"))
        @route_inline_menu.message(F.text.lower() == 'анекдот')
        async def create_inline_text_main(message: types.Message) -> None:
            check_user = self.manager_users.check_user(id_account = message.from_user.id)
            if check_user == self.manager_users.state_user[0] or check_user == self.manager_users.state_user[1]:
                get_text = get_anecdote()
                id_anecdote = random.randint(1, self.len_list_anecdotes)
                command_text = "\n\n Показать еще /anecdote"
                text = get_text(id_anecdote) + command_text
                await message.answer(text = text)
            elif check_user == self.manager_users.state_user[3]:
                await message.answer('Вы не зарегистрированы! Выполните команду /registration')
            elif check_user== self.manager_users.state_user[2]:
                await message.answer('Вы в черном списке!')
            