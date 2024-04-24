# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий класс KeyWord."""

from .table import Table
from .data_for_tables.data_key_word import key_word_data as data
from .query_for_tables.query_key_word import query_create, query_insert, query_on_menu_name

class KeyWord(Table):
    """! Класс-таблица KeyWord
    """    
    def __init__(self, name_db: str) -> None:
        super().__init__(name_db = name_db)
        ## Запрос создания таблицы.
        self.create_query = query_create
        ## Данные для добавления в таблицу.
        self.data_to_db = data
        ## Запрос добавления в таблицу.
        self.query_insert = query_insert
        ## Запрос выборки ключевых слов по названию меню.
        self.query_on_menu_name = query_on_menu_name

    def select_on_menu_name(self, name_menu: str) -> list[str]:
        """! Функция выборки ключевых слов по названию меню.

        @param menu_name - название меню.

        Переменные:
            1. all_results - записи выборки из базы данных.

        @return Список ключевых слов для меню.
        """
        self.connect_db()
        self.cursor.execute(self.query_on_menu_name, (name_menu,))
        all_results=self.cursor.fetchall()
        self.sqlite_connection.close()
        return self.parser_on_menu_name(all_results)
    
    def parser_on_menu_name(self, all_results: list[list[str]]) -> list[str]:
        """! Функция подготовки списка ключевых слов.

        @param all_results - записи выборки из базы данных.

        Переменные:
            1. key_words - список ключевых слов.

        @return key_words - список ключевых слов.
        """
        key_words = list()
        for k in all_results:
            key_words.append(k[0])
        return key_words 