# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий класс ListUsers."""

from .table import Table
from .data_for_tables.data_list_users import list_users_data as data
from .query_for_tables.query_list_users import query_create, query_insert
from .query_for_tables.query_list_users import query_update_admin, query_update_ban, query_update_notban

class ListUsers(Table):
    """! Класс-таблица class ListUsers(Table):
    """    
    def __init__(self, name_db: str) -> None:
        super().__init__(name_db = name_db)
        ## Запрос создания таблицы.
        self.create_query = query_create
        ## Данные для добавления в таблицу.
        self.data_to_db = data
        ## Запрос добавления в таблицу.
        self.query_insert = query_insert
        ## Запрос изменения категории пользователя на "Администратор".
        self.query_update_admin = query_update_admin
        ## Запрос изменения категории пользователя на "Черный список".
        self.query_update_ban = query_update_ban
        ## Запрос изменения категории пользователя на "Обычный пользователь".
        self.query_update_notban = query_update_notban

    def update_ban(self, id_account) -> None:
        """! Функция изменения категории пользователя на "Черный список".

        @param id_account - id аккаунта пользователя.
        """
        self.connect_db()
        self.cursor.execute(self.query_update_ban, (id_account,))
        self.sqlite_connection.commit()
        self.close_connect_db()

    def update_notban(self, id_user) -> None:
        """! Функция изменения категории пользователя на "Обычный пользователь".

        @param id_account - id аккаунта пользователя.
        """
        self.connect_db()
        self.cursor.execute(self.query_update_notban, (id_user,))
        self.sqlite_connection.commit()
        self.close_connect_db()

    def update_admin(self, id_user) -> None:
        """! Функция изменения категории пользователя на "Администратор".

        @param id_account - id аккаунта пользователя.
        """
        self.connect_db()
        self.cursor.execute(self.query_update_admin, (id_user,))
        self.sqlite_connection.commit()
        self.close_connect_db()