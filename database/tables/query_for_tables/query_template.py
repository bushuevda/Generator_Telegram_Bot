# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий запросы к таблице Template."""

#запрос создание таблицы Template
query_create = """
    CREATE TABLE Template
    (id_template INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    name_template TEXT NOT NULL);
"""

#запрос добавления в таблицу Template
query_insert = "INSERT INTO Template (name_template) VALUES(?);" 