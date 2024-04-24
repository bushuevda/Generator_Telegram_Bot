# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий запросы к таблице Type_Menu."""

#запрос создание таблицы Type_Menu
query_create = """
    CREATE TABLE Type_Menu
    (id_type_menu INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    type_menu TEXT NOT NULL);
"""

#запрос добавления в таблицу Type_Menu
query_insert = "INSERT INTO Type_Menu (type_menu) VALUES(?);" 
