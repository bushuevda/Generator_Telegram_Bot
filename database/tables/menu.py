# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий класс Menu."""

from .table import Table
from .data_for_tables.data_menu import menu_data as data
from .query_for_tables.query_menu import query_create, query_insert, query_select_all
from .query_for_tables.query_menu import query_select_menu_on_callback, query_select_menu_on_type 
from .query_for_tables.query_menu import query_select_menu_on_id_button

class Menu(Table):
    """! Класс-таблица Menu
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
        ## Запрос выборки информации о меню по callback кнопки.
        self.query_select_menu_on_callback = query_select_menu_on_callback
        ## Запрос выборки информации о меню по типу меню.
        self.query_select_menu_on_type = query_select_menu_on_type
        ## Запрос выборки информации о меню по id кнопки.
        self.query_select_menu_on_id_button = query_select_menu_on_id_button

    def select_menu_on_callback(self, cb_data: str) -> list:
        """! Функция выборки информации о меню по callback кнопки.

        @param cb_data - callback кнопки.

        Переменные:
            1. all_results - записи выборки из базы данных.

        @return Список информации о меню.
        """
        self.connect_db()
        self.cursor.execute(self.query_select_menu_on_callback, (cb_data,))
        all_results = self.cursor.fetchall()
        self.close_connect_db()
        return all_results      

    def select_menu_on_type(self, id_type_menu: int) -> list:
        """! Функция выборки информации о меню по типу меню.

        @param id_type_menu - id типа меню.

        Переменные:
            1. all_results - записи выборки из базы данных.

        @return Список информации о меню.
        """
        self.connect_db()
        self.cursor.execute(self.query_select_menu_on_type, (id_type_menu,))
        all_results = self.cursor.fetchall()
        self.close_connect_db()
        return all_results    

    def select_menu_on_id_button(self, id_button: int) -> list:
        """! Функция выборки информации о меню по id кнопки.

        @param id_button - id кнопки.

        Переменные:
            1. all_results - записи выборки из базы данных.

        @return Список информации о меню.
        """
        self.connect_db()
        self.cursor.execute(self.query_select_menu_on_id_button, (id_button,))
        all_results = self.cursor.fetchall()
        self.close_connect_db()
        return all_results    