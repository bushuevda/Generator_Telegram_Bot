# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).

"""! @brief Пакет содержащий классы Registration, Admin, ReplyMenu, которые отвечают за администрирование и меню reply."""

from aiogram.types import  KeyboardButton, ReplyKeyboardMarkup, WebAppInfo, Message
from aiogram import Router, types, Bot, F
from aiogram.filters.command import Command
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State

router_reply_menu = Router()

class Registration(StatesGroup):
    """! Класс событий регистрации пользователя.
    """
    ## статус изменения пароля регистрации
    state_registration = State()

class Admin(StatesGroup):
    """! Класс событий изменения категории пользователя.
    """
    ## статус ввода id аккаунта пользователя
    state_category_enter_id_account = State()
    ## статус ввода id новой категории пользователя
    state_category_enter_id_category = State()
    ## статус изменения id категории пользователя
    state_change_registration_password = State()

class ReplyMenu:
    """! Класс создания меню reply и событий конечных автоматов.
    """
    def __init__(self, answer_message: str, command: str , manager_users: object, registration_password: str) -> None:
        ## Сообщение при выполнении команды вызова меню reply.
        self.answer_message = answer_message
        ## Команда для вызова меню reply.
        self.command = command
        ## Класс-менеджер пользователей.
        self.manager_users = manager_users
        ## Пароль для регистрации пользователей.
        self.registration_password = registration_password

    def create(self, keyboard: list[list[ReplyKeyboardMarkup]]) -> None:
        """! Функция создает наблюдателя за выполнением команды для вывода меню reply.

        @param keyboard -  список кнопок меню.

        Переменные:
            1. formed_keyboard - сформированное меню
            2. check_user - результат проверки пользователя (False, True).
        
        Условие:
            1. Если пользователь в черном списке или не зарегистрирован вывод соответствующего сообщения.
        """
        @router_reply_menu.message(Command(self.command))
        async def cmd_start(message: types.Message):
            check_user = self.manager_users.check_user(id_account = message.from_user.id)
            if check_user == self.manager_users.state_user[0] or check_user == self.manager_users.state_user[1]:   
                formed_keyboard = ReplyKeyboardMarkup(keyboard = keyboard)
                await message.answer(self.answer_message, reply_markup = formed_keyboard)
            elif self.manager_users.check_user(id_account = message.from_user.id) == self.manager_users.state_user[3]:
                await message.answer('Вы не зарегистрированы! Выполните команду /registration')
            elif self.manager_users.check_user(id_account = message.from_user.id) == self.manager_users.state_user[2]:
                await message.answer('Вы в черном списке!')

          
    def registration(self) -> None:
        """! Функция создает наблюдателя за началом событий регистрации с помощью заданной команды.

        Функции:
            1. registration_start - событие начала регистрации.
            2. registration_end - событие завершения регистрации.

        Переменные:
            1. check_user - результат проверки пользователя (False, True).
        
        Условие:
            1. Если пользователь ввел неверный пароль или уже зарегистрирован вывод соответствующего сообщения.
        """
        @router_reply_menu.message(Command("registration"))
        async def registration_start(message: types.Message, state: FSMContext) -> None:
            check_user = self.manager_users.check_user(id_account = message.from_user.id)
            if check_user == self.manager_users.state_user[3]: 
                await message.answer("Введите пароль:")
                await state.set_state(Registration.state_registration)
            else:
                await message.answer('Вы уже зарегистрированы!')
            
        @router_reply_menu.message(Registration.state_registration)
        async def registration_end(message: types.Message, state: FSMContext) -> None:
            check_user = self.manager_users.check_user(id_account = message.from_user.id)
            if check_user == self.manager_users.state_user[3]: 
                if str(self.registration_password) == message.text:
                    self.manager_users.registration(message.from_user.username, message.from_user.id)
                    await message.answer(f'{message.from_user.username}, вы успешно зарегистрированы,' +
                                         'для начала работы введите команду /start')
                else:
                    await message.answer('Неверный пароль! Повторите попытку /registration')
            else:
                await message.answer('Вы уже зарегистрированы!')                    
            await state.clear()

            
    def admin(self) -> None:
        """! Функция создает меню администратора и обработчики событий при нажатии кнопок.

        Функции:
            1. create_admin_panel - создание меню администратора.
            2. get_list_users_ban - получение списка пользователей категории "Черный список".
            3. get_list_users_unsual - получение списка пользователей категории "Обычный пользователь".
            4. get_list_users_admin - получение списка пользователей категории "Администратор".
            5. get_password_registration - получение пароля для регистрации.
            6. change_password_registration_start - начало события изменения пароля регистрации - ввод пароля регистрации.
            7. change_password_registration_end - завершение события изменения пароля регистрации.
            8. change_category_user_start - начало события изменения категории пользователя - ввод id аккаунта пользователя.
            9. enter_category_user - ввод id новой категории пользователя.
            10. change_category_user_end - завершение события изменения категории пользователя.

        Условие:
            1. Если пользователь не является администратором вывод соответствующего сообщения.
        """
        @router_reply_menu.message(Command("admin"))
        async def create_admin_panel(message: types.Message) -> None:
            # результат проверки пользователя (False, True)
            check_user = self.manager_users.check_user(id_account = message.from_user.id)
            if check_user == self.manager_users.state_user[1]: 
                # список кнопок меню
                keyboard_admin = [
                    [KeyboardButton(text="Показать черный список")],
                    [KeyboardButton(text="Показать обычных пользователей")],
                    [KeyboardButton(text="Показать администраторов")],
                    [KeyboardButton(text="Показать пароль для регистрации")],
                    [KeyboardButton(text="Изменить категорию пользователя")],
                    [KeyboardButton(text="Изменить пароль для регистрации")],
                ]
                # сформированное меню
                formed_keyboard = ReplyKeyboardMarkup(keyboard = keyboard_admin)
                await message.answer(self.answer_message, reply_markup = formed_keyboard)
            else:
                await message.answer('Вы не являетесь администратором!')
        
        # функция вывода списка пользователей черного списка
        @router_reply_menu.message(F.text == 'Показать черный список')
        async def get_list_users_ban(message: types.Message) -> None:
            # результат проверки пользователя (False, True)
            check_user = self.manager_users.check_user(id_account = message.from_user.id)
            if check_user == self.manager_users.state_user[1]:   
                # список пользователей категории "Черный список"
                str_ban_users = self.manager_users.get_ban_users()
                await message.answer(str_ban_users)
            else:
                await message.answer('Вы не являетесь администратором!')

        # функция вывода списка обычных пользователей
        @router_reply_menu.message(F.text == 'Показать обычных пользователей')
        async def get_list_users_unsual(message: types.Message) -> None:
            # результат проверки пользователя (False, True)
            check_user = self.manager_users.check_user(id_account = message.from_user.id)
            if check_user == self.manager_users.state_user[1]: 
                # список пользователей категории "Обычный пользователь"  
                str_usual_users = self.manager_users.get_usual_users()
                await message.answer(str_usual_users)
            else:
                await message.answer('Вы не являетесь администратором!')

        # функция вывода списка администраторов
        @router_reply_menu.message(F.text == 'Показать администраторов')
        async def get_list_users_admin(message: types.Message) -> None:
            # результат проверки пользователя (False, True)
            check_user = self.manager_users.check_user(id_account = message.from_user.id)
            if check_user == self.manager_users.state_user[1]:  
                 # список пользователей категории "Администратор" 
                str_admin_users = self.manager_users.get_admin_users()
                await message.answer(str_admin_users)
            else:
                await message.answer('Вы не являетесь администратором!')

        # функция вывода пароля регистрации
        @router_reply_menu.message(F.text == 'Показать пароль для регистрации')
        async def get_password_registration(message: types.Message) -> None:
            # результат проверки пользователя (False, True)
            check_user = self.manager_users.check_user(id_account = message.from_user.id)
            if check_user == self.manager_users.state_user[1]:   
                await message.answer(self.registration_password)
            else:
                await message.answer('Вы не являетесь администратором!')

        # События изменения пароля регистрации
        # функция запроса ввода пароля для регистрации
        @router_reply_menu.message(F.text == 'Изменить пароль для регистрации')
        async def change_password_registration_start(message: types.Message, state: FSMContext) -> None:
            # результат проверки пользователя (False, True)
            check_user = self.manager_users.check_user(id_account = message.from_user.id)
            if check_user == self.manager_users.state_user[1]:   
                await message.answer("Введите новый пароль для регистрации:")
                await state.set_state(Admin.state_change_registration_password)
            else:
                await message.answer('Вы не являетесь администратором!')
                
        # функция изменения пароля для регистрации
        @router_reply_menu.message(Admin.state_change_registration_password)
        async def change_password_registration_end(message: types.Message, state: FSMContext) -> None:
            # результат проверки пользователя (False, True)
            check_user = self.manager_users.check_user(id_account = message.from_user.id)
            if check_user == self.manager_users.state_user[1]: 
                # новый пароль регистрации
                self.registration_password = message.text  
                await message.answer(f"Пароль успешно изменен. Новый пароль для регистрации: {self.registration_password}")
                await state.clear()
            else:
                await message.answer('Вы не являетесь администратором!')
        
        #События изменения категории пользователя
        # функция запроса ввода id аккаунта пользователя
        @router_reply_menu.message(F.text == 'Изменить категорию пользователя')
        async def change_category_user_start(message: types.Message, state: FSMContext) -> None:
            # результат проверки пользователя (False, True)
            check_user = self.manager_users.check_user(id_account = message.from_user.id)
            if check_user == self.manager_users.state_user[1]:   
                await message.answer("Введите id аккаунта пользователя:")
                await state.set_state(Admin.state_category_enter_id_account)
            else:
                await message.answer('Вы не являетесь администратором!')

        # функция запроса ввода новой категории для пользователя
        @router_reply_menu.message(Admin.state_category_enter_id_account)
        async def enter_category_user(message: types.Message, state: FSMContext)  -> None:
            # результат проверки пользователя (False, True)
            check_user = self.manager_users.check_user(id_account = message.from_user.id)
            if check_user == self.manager_users.state_user[1]: 
                await state.update_data(id_account = message.text)
                if message.text.isnumeric():
                    if self.manager_users.get_user_name(int(message.text)):
                        await message.answer("Выберите категорию: \n 1 - Пользователь \n 2 - Администратор \n 3 - Черный список")
                        await state.set_state(Admin.state_category_enter_id_category)
                    else:
                        await message.answer('Пользователь с таким id отсутствует!')
                else:
                    await message.answer('Неправильный ввод, необходимо ввести число! Операция прервана.')
                    await state.clear()
            else:
                await message.answer('Вы не являетесь администратором!')

        # функция изменения категории пользователя
        @router_reply_menu.message(Admin.state_category_enter_id_category)
        async def change_category_user_end(message: types.Message, state: FSMContext) -> None:
            # результат проверки пользователя (False, True)
            check_user = self.manager_users.check_user(id_account = message.from_user.id)
            if check_user == self.manager_users.state_user[1]: 
                # id аккаунта пользователя   
                id_account = await state.get_data()
                # имя пользователя
                user_name = self.manager_users.get_user_name(int(id_account["id_account"]))
                # id новой категории пользователя
                # 1 - 'Обычный пользователь', 2 - 'Администратор', 3 - 'Черный список'
                category = message.text
                if id_account and category in ['1', '2', '3']:
                    if category == '1':    
                        self.manager_users.pop_ban(id_account["id_account"])
                    elif category == '2':
                        self.manager_users.set_admin(id_account["id_account"])
                    elif category == '3':
                        self.manager_users.push_ban(id_account["id_account"])
                    await message.answer(f"Категория для пользователь с id ={id_account['id_account']} " +
                                         f"и с user_name = {user_name} изменена на категорию под номером {message.text}")
                    await state.clear()
                else:
                    await message.answer('Неправильный ввод, необходимо ввести число! Операция прервана')
                    await state.clear()
            else:
                await message.answer('Вы не являетесь администратором!')
