# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий класс ManagerUsers."""

from .tables import User, ListUsers

class ManagerUsers:
    """! Класс манипулирования информации о пользователях.
    """
    def __init__(self, dict_users: dict, name_db: str) -> None:
        ## Словарь пользователей.
        self.dict_user = dict_users
        ## Объект класса User.
        self.table_user = User(name_db = name_db)
        ## Объект класса ListUsers.
        self.table_list_users = ListUsers(name_db = name_db)
        ## Состояния пользователей.
        self.state_user = ('пользователь', 'администратор', 'черный список', 'не зарегистрирван',)

    def get_users(self) -> dict:
        """! Функция получения словаря пользователей.

        @return Словарь пользователей.
        """
        return self.dict_user

    def get_user_name(self, id_account: int) -> str:
        """! Функция получения имени пользователя по id аккаунта.

        @param id_account - id аккаунта.

        @return Имя пользователя.
        """
        return self.dict_user.get(id_account)
    
    def check_user(self, id_account: int) -> str:
        """! Функция получения статуса пользователя.

        @param id_account - id аккаунта.

        Переменные:
            1. state_check - категория пользователя.
        
        Условия:
            1. Если str.lower(state_check[0][0]) == self.state_user[0], то возвращается статус 'Обычный пользователь'.
            2. Если str.lower(state_check[0][0]) == self.state_user[0], то возвращается статус 'Администратор'.
            3. Если str.lower(state_check[0][0]) == self.state_user[0], то возвращается статус 'Черный список'.

        @return self.state_user.
        """
        state_check = self.table_user.select_category_on_id_account(id_account = id_account)
        if len(state_check) > 0:
            if str.lower(state_check[0][0]) == self.state_user[0]:
                return self.state_user[0]
            elif str.lower(state_check[0][0]) == self.state_user[1]:
                return self.state_user[1]
            elif str.lower(state_check[0][0]) == self.state_user[2]:
                return self.state_user[2]
        else:
            return self.state_user[3]
        
    def registration(self, name_user: str, id_account: int) -> None:
        """! Функция регистрации пользователя.

        @param name_user - имя пользователя.
        @param id_account - id аккаунта.

        Переменные:
            1. id_last_user - id последнего пользователя в базе данных.
        """
        if name_user and id_account:
            self.table_user.insert_user(name_user, id_account)
            id_last_user = self.table_user.get_last_row() 
            self.table_list_users.insert((id_last_user, 1))
            self.dict_user[id_account] = name_user
        
    def push_ban(self, id_account: int) -> None:
        """! Функция добавления пользователя в категорию 'Черный список'.

        @param id_account - id аккаунта.

        Переменные:
            1. id_user - id пользователя.
        """
        if id_account:
            id_user = self.table_user.select_id_user_on_id_account(id_account = id_account)
            if id_user:
                self.table_list_users.update_ban(id_user = id_user[0][0])
    
    def pop_ban(self, id_account: int) -> None:
        """! Функция добавления пользователя в категорию 'Обычный пользователь'.

        @param id_account - id аккаунта.

        Переменные:
            1. id_user - id пользователя.
        """
        if id_account:
            id_user = self.table_user.select_id_user_on_id_account(id_account = id_account)
            if id_user:
                self.table_list_users.update_notban(id_user = id_user[0][0])

    def set_admin(self, id_account: int) -> None:
        """! Функция добавления пользователя в категорию 'Администратор'.

        @param id_account - id аккаунта.

        Переменные:
            1. id_user - id пользователя.
        """
        if id_account:
            id_user = self.table_user.select_id_user_on_id_account(id_account = id_account)
            if id_user:
                self.table_list_users.update_admin(id_user = id_user[0][0])
    
    def get_admin_users(self) -> str:
        """! Функция получения пользователей  категории 'Администратор'.

        @return Пользователи категории 'Администратор'.
        """
        return self.parser_list_users(self.table_user.select_user_on_category('Администратор'), title = 'Администраторы:\n')

    def get_ban_users(self) -> str:
        """! Функция получения пользователей  категории 'Черный список'.

        @return Пользователи категории 'Черный список'.
        """
        return self.parser_list_users(self.table_user.select_user_on_category('Черный список'), title = 'Черный список:\n')

    def get_usual_users(self) -> str:
        """! Функция получения пользователей  категории 'Обычный пользователь'.

        @return Пользователи категории 'Обычный пользователь'.
        """
        return self.parser_list_users(self.table_user.select_user_on_category('Пользователь'), title = 'Обычные пользователи:\n')

    def parser_list_users(self, list_users: list[str], title: str) -> str:
        """! Функция формирования строки списка пользователей для определенной категории.
        
        @param list_users - список пользователей определенной категории.
        @param title - название категории.

        @return Пользователи определенной категории.
        """
        str_parsed = title
        for k in list_users:
            str_parsed = str_parsed + str(k[0]) + "  -  " + str(k[1]) + "\n"
        return str_parsed

