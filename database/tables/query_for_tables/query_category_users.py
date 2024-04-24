# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий запросы к таблице Category_Users."""

#запрос создание таблицы Category_Users
query_create = """
    CREATE TABLE Category_Users
    (id_category_users INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    name_category TEXT NOT NULL UNIQUE);
"""

#запрос добавления в таблицу Category_Users
query_insert = "INSERT INTO Category_Users (name_category) VALUES(?);" 