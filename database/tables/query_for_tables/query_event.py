# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий запросы к таблице Event."""

#запрос создание таблицы Event
query_create = """
    CREATE TABLE Event
    (id_event INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    name_event TEXT NOT NULL UNIQUE);
"""
#запрос добавления в таблицу Event
query_insert = "INSERT INTO Event(name_event) VALUES(?);" 

#запрос выборки всех записей из таблицы Event
query_select_all = "SELECT * FROM Event;"

