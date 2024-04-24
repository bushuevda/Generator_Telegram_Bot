# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий класс ListInformation."""

from .table import Table
from .data_for_tables.data_list_information import list_information_data as data
from .query_for_tables.query_list_information import query_create, query_insert

class ListInformation(Table):
    """! Класс-таблица ListInformation
    """    
    def __init__(self, name_db: str) -> None:
        super().__init__(name_db = name_db)
        ## Запрос создания таблицы.
        self.create_query = query_create
        ## Данные для добавления в таблицу.
        self.data_to_db = data
        ## Запрос добавления в таблицу.
        self.query_insert = query_insert
