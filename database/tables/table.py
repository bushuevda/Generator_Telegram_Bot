# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий абстрактный класс Table."""

from abc import ABC
import sqlite3

class Table(ABC):
    """! Абстрактный класс-таблица.
    """    
    def __init__(self, name_db: str) -> None:
        ## Запрос создания таблицы.
        self.name_db: str = name_db
        ## Объект соединения с базой данных.
        self.sqlite_connection: sqlite3.Connection = None
        ## Объект взаимодействия с базой данных.
        self.cursor: sqlite3.Cursor = None
        ## Запрос создания таблицы.
        self.create_query: str = None
        ## Запрос выборки последней записи из таблицы.
        self.query_last_row: str = None
        ## Данные для добавления в таблицу.
        self.data_to_db: list[list] = None
        ## Запрос добавления в таблицу.
        self.query_insert: str = None
        ## Запрос выборки всех записей таблицы.
        self.query_select_all = None

    def connect_db(self) -> None:
        """! Функция соединения с базой данных.
        """
        self.sqlite_connection=sqlite3.connect(self.name_db)
        self.cursor = self.sqlite_connection.cursor()
           
    def close_connect_db(self) -> None:
        """! Функция закрытия соединения с базой данных.
        """
        self.sqlite_connection.close()

    def select_all(self) -> list:
        """! Функция выборки всех записей таблицы.

        Переменные:
            1. all_results - записи выборки из базы данных.

        @return all_results - записи выборки из базы данных.
        """
        self.connect_db()
        self.cursor.execute(self.query_select_all,)
        all_results = self.cursor.fetchall()
        self.close_connect_db()
        return all_results    
    
    def insert(self, *args) -> None:
        """! Функция добавления информации в таблицу.
        @param *args - аргументы для добавления в таблицу.
        """        
        self.connect_db()
        self.cursor.executemany(self.query_insert,args)
        self.sqlite_connection.commit()
        self.close_connect_db()
    
    def insert_data(self) -> None:
        """! Функция добавления данных в таблицу.

        Переменные:
            1. data - список информации для добавления в таблицу.
            2. data_add - данные для формирования списка информации.
        """      
        for get_data in self.data_to_db:
            data = list()
            for data_add in get_data:
                data.append(data_add)
            print(data)
            self.insert(data)
            
    def update(self, query: str) -> None:
        """! Функция изменения информации в таблице.

        @param query - запрос к базе данных.
        """    
        self.connect_db()
        self.cursor.execute(query)
        self.sqlite_connection.commit()
        self.close_connect_db()

    def create(self) -> None:
        """! Функция создания таблицы.
        """    
        self.connect_db()
        self.cursor.execute(self.create_query)
        self.sqlite_connection.commit()
        self.close_connect_db()
    
    def get_last_row(self) -> int:
        """! Функция выборки последней записи из таблицы.

        Переменные:
            1. result - результат выборки последней записи таблицы.
        
        Условия:
            1. Если result не пустой возвращается id последней записи таблицы.
            2. Если result пустой возвращается 1.
        """ 
        self.connect_db()
        self.cursor.execute(self.query_last_row)
        result = self.cursor.fetchone()
        self.close_connect_db()
        if result:
            return int(result[0])
        else:
            return 1

