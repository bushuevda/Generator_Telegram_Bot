# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий запросы к таблице Type_Information."""

#запрос создание таблицы Type_Information
query_create = """
    CREATE TABLE Type_Information
    (id_type_information INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    name_type TEXT NOT NULL);
"""

#запрос добавления в таблицу Type_Information
query_insert = "INSERT INTO Type_Information (name_type) VALUES(?);" 