# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий класс Button."""

from .table import Table
from .data_for_tables.data_button import button_data as data
from .query_for_tables.query_button import query_create, query_insert, query_on_menu_name
from .query_for_tables.query_button import query_on_callback_data, query_select_all
from typing import Union

class Button(Table):
    """! Класс-таблица Button
    """    
    def __init__(self,name_db: str) -> None:
        super().__init__(name_db = name_db)
        ## Запрос создания таблицы.
        self.create_query = query_create
        ## Данные для добавления в таблицу.
        self.data_to_db = data
        ## Запрос добавления в таблицу.
        self.query_insert = query_insert
        ## Запрос выборки кнопок по названию меню.
        self.query_on_menu_name = query_on_menu_name
        ## Запрос выборки кнопок для меню по callback_data.
        self.query_on_callback_data = query_on_callback_data
        ## Запрос выборки всех записей таблицы.
        self.query_select_all = query_select_all
        
    def select_on_menu_name(self, menu_name: str) -> list[str]:
        """! Функция выборки кнопок по названию меню.

        @param menu_name - название меню.

        Переменные:
            1. all_results - записи выборки из базы данных.

        @return Сформированный список информации о кнопках.
        """
        self.connect_db()
        self.cursor.execute(self.query_on_menu_name, (menu_name,))
        all_results = self.cursor.fetchall()
        self.sqlite_connection.close()
        return self.parser_in_union(all_results)

    def select_on_callback_data(self, cb_data: str) -> list[str]: 
        """! Функция выборки информации о кнопке по callback.

        @param cb_data - название меню.

        Переменные:
            1. all_results - записи выборки из базы данных.

        @return Сформированный список информации о кнопке.
        """
        self.connect_db()
        self.cursor.execute(self.query_on_callback_data, (cb_data,))
        all_results = self.cursor.fetchall()
        self.sqlite_connection.close()
        return self.parser_in_union(all_results)

    def parser_in_union(self, all_results: list[list[str]]) -> Union [list[str], list[str], list[str]]: 
        """! Функция объдинения списков информации о кнопках для .

        @param all_results - записи выборки из базы данных.

        Переменные:
            1. counts_buttons - количество кнопок в ряду.
            2. name_button - названия кнопок.
            3. callback_buttons - callback кнопок.

        @return Объединенные списки информации о кнопках.
        """
        counts_buttons = list()
        name_buttons = list()
        callback_buttons = list()
        for k in all_results:
            name_buttons.append(k[0])
            callback_buttons.append(k[1])
            counts_buttons.append(k[2])
        return name_buttons, callback_buttons, counts_buttons    