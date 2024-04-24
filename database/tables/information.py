# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий класс Inforamtion."""

from .table import Table
from .data_for_tables.data_information import information_data as data
from .query_for_tables.query_information import query_create, query_insert
from .query_for_tables.query_information import query_on_menu_name_file, query_on_menu_name_image
from .query_for_tables.query_information import query_on_menu_name_text

class Inforamtion(Table):
    """! Класс-таблица Inforamtion
    """    
    def __init__(self, name_db: str) -> None:
        super().__init__(name_db = name_db)
        ## Запрос создания таблицы.
        self.create_query = query_create
        ## Данные для добавления в таблицу.
        self.data_to_db = data
        ## Запрос добавления в таблицу.
        self.query_insert = query_insert
        ## Запрос выборки пути к файлу по названию меню.
        self.query_on_menu_name_file = query_on_menu_name_file
        ## Запрос выборки пути к изображению или изображениям по названию меню.
        self.query_on_menu_name_image = query_on_menu_name_image
        ## Запрос выборки текста по названию меню.
        self.query_on_menu_name_text = query_on_menu_name_text

    def select_on_menu_name_file(self, name_menu: str) -> list[str]:
        """! Функция выборки пути к файлу по названию меню.

        @param menu_name - название меню.

        Переменные:
            1. all_results - записи выборки из базы данных.

        @return Путь к файлу.
        """
        self.connect_db()
        self.cursor.execute(self.query_on_menu_name_file, (name_menu,))
        all_results = self.cursor.fetchall()
        self.sqlite_connection.close()
        return self.parser_all_results(all_results)

    def select_on_menu_name_image(self, name_menu: str, mod_all = False) -> list[str]:
        """! Функция выборки пути к изображению или изображениям по названию меню.

        @param menu_name - название меню.

        Переменные:
            1. all_results - записи выборки из базы данных.

        @return Путь к изображению или изображениям.
        """
        self.connect_db()
        self.cursor.execute(self.query_on_menu_name_image, (name_menu,))
        all_results = self.cursor.fetchall()
        self.sqlite_connection.close()
        return self.parser_all_results(all_results, mod_all)

    def select_on_menu_name_text(self, name_menu: str, mod_all = False) -> list[str]:
        """! Функция выборки текста по названию меню.

        @param menu_name - название меню.

        Переменные:
            1. all_results - записи выборки из базы данных.

        @return Текст.
        """
        self.connect_db()
        self.cursor.execute(self.query_on_menu_name_text, (name_menu,))
        all_results = self.cursor.fetchall()
        self.sqlite_connection.close()
        return self.parser_all_results(all_results, mod_all = mod_all)

    def parser_all_results(self, all_results: list[list[str]], mod_all = False) -> str:
        """! Функция подготовки информации.

        @param new_list - информация для возвращения.
        @param mod_all - флаг для выбора возвращения типа (строки или списка).

        Переменные:
            1. new_list - информация для возвращения.

        Условия:
            1. Если new_list пустой, то в список new_list добавляется пустая строка.
            2. Если mod_all == False возвращается строка.
            3. Если mod_all == True возвращется список.
            
        @return new_list - информация для возвращения.
        """
        new_list = list() 
        for k in all_results:
            new_list.append(k[0]) 
        if not new_list:
            new_list.append(' ')
        if not mod_all:
            return new_list[0]
        else:
            return new_list

