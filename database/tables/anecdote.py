# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий класс Anecdote."""

from .table import Table
from .data_for_tables.data_anecdote import anecdote_data as data 
from .query_for_tables.query_anecdote import query_create, query_insert
from .query_for_tables.query_anecdote import query_select_anecdot_on_id, query_last_row

class Anecdote(Table):
    """! Класс-таблица Anecdote
    """
    def __init__(self,name_db: str) -> None:
        super().__init__(name_db = name_db)
        ## Запрос создания таблицы.
        self.create_query = query_create
        ## Данные для добавления в таблицу.
        self.data_to_db = data
        ## Запрос добавления в таблицу.
        self.query_insert = query_insert
        ## Запрос выборки анекдота из таблицы по id
        self.query_select_anecdot_on_id = query_select_anecdot_on_id
        ## Запрос выборки последней записи из таблицы
        self.query_last_row = query_last_row

    def select_anecdote_on_id(self, id_anecdote: int) -> str: 
        """! Функция выборки анекдота по id.

        @param id_anecdote - id анекдота.

        Переменные:
            1. all_results - записи выборки из базы данных.

        @return Текст анекдота.
        """
        self.connect_db()
        self.cursor.execute(self.query_select_anecdot_on_id, (id_anecdote,))
        all_results = self.cursor.fetchall()
        self.sqlite_connection.close()
        return self.parser_select_anecdote_on_id(all_results)

    def parser_select_anecdote_on_id(self, all_results: list[list[str]]) -> str: 
        """! Функция выборки анекдота по id.

        @param all_results - записи выборки из базы данных.

        Переменные:
            1. anecdote_text - текст анекдота.

        @return anecdote_text - текст анекдота.
        """
        anecdote_text = str()
        if len(all_results) >= 1:
            anecdote_text = all_results[0][0]
        return anecdote_text