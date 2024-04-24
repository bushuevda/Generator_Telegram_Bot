# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий класс User."""

from .table import Table
from .data_for_tables.data_user import user_data as data
from .query_for_tables.query_user import query_create, query_insert, query_select_all
from .query_for_tables.query_user import query_select_id_user_on_id_account, query_select_category_on_id_account
from .query_for_tables.query_user import query_select_user_on_category, query_last_row

class User(Table):
    """! Класс-таблица User
    """  
    def __init__(self, name_db: str) -> None:
        super().__init__(name_db = name_db)
         ## Запрос создания таблицы.
        self.create_query = query_create
        ## Данные для добавления в таблицу.
        self.data_to_db = data
        ## Запрос добавления в таблицу.
        self.query_insert = query_insert
        ## Запрос выборки всех записей таблицы.
        self.query_select_all = query_select_all
        ## Запрос выборки id пользователя по id аккаунта.
        self.query_select_id_user_on_id_account = query_select_id_user_on_id_account
        ## Запрос выборки категории пользователя по id аккаунта.
        self.query_select_category_on_id_account = query_select_category_on_id_account
        ## Запрос выборки последней записи из таблицы.
        self.query_last_row = query_last_row
        ## Запрос выборки пользователей по категории.
        self.query_select_user_on_category = query_select_user_on_category

    def select_on_parser(self) -> dict:
        """! Функция выборки всех пользователей.

        Переменные:
            1. users_dict - словарь всех пользователей ("id_account" : "name_account").

        @return users_dict
        """    
        users_dict = dict()
        for user in self.select_all():
            users_dict[int(user[1])] = user[0]
        return users_dict
    
    def insert_user(self, name_account: str, id_account: int) -> None:
        """! Функция добавления пользователя.

        @param name_account - имя пользователя.
        @param id_account - id аккаунта.
        """    
        self.connect_db()
        self.cursor.execute(self.query_insert, (name_account, id_account))
        self.sqlite_connection.commit()
        self.close_connect_db()
    
    def select_id_user_on_id_account(self, id_account: int) -> list[list]:
        """! Функция выборки id пользователя по id аккаунта.

        @param id_account - id аккаунта.

        Переменные:
            1. all_results - записи выборки из базы данных.

        @return - all_results - записи выборки из базы данных.
        """    
        self.connect_db()
        self.cursor.execute(self.query_select_id_user_on_id_account, (id_account,))
        all_results = self.cursor.fetchall()
        self.close_connect_db()
        return all_results    
    
    def select_category_on_id_account(self, id_account: int) -> list[list]:
        """! Функция выборки категории пользователя по id аккаунта.

        @param id_account - id аккаунта.

        Переменные:
            1. all_results - записи выборки из базы данных.

        @return - all_results - записи выборки из базы данных.
        """   
        self.connect_db()
        self.cursor.execute(self.query_select_category_on_id_account, (id_account, ))
        all_results = self.cursor.fetchall()
        self.close_connect_db()
        return all_results    

    def select_user_on_category(self, category_name: str) -> list[list]:
        """! Функция выборки категории пользователей по категории.

        @param category_name - название категории.

        Переменные:
            1. all_results - записи выборки из базы данных.

        @return - all_results - записи выборки из базы данных.
        """   
        self.connect_db()
        self.cursor.execute(self.query_select_user_on_category, (category_name, ))
        all_results = self.cursor.fetchall()
        self.close_connect_db()
        return all_results    