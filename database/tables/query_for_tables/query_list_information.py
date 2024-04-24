# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий запросы к таблице List_Information."""

#запрос создание таблицы List_Information
query_create = """
    CREATE TABLE List_Information
    (id_list_information INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL,
    id_menu INTEGER NOT NULL,
    id_information INTEGER NOT NULL,
    id_type_information INTEGER NOT NULL,
    FOREIGN KEY (id_menu) REFERENCES Menu(id_menu),
    FOREIGN KEY (id_information) REFERENCES Information(id_information),
    FOREIGN KEY (id_type_information) REFERENCES Type_Information(id_type_information));
"""

#запрос добавления в таблицу List_Information
query_insert = "INSERT INTO List_Information (id_menu, id_information, id_type_information) VALUES(?, ?, ?);" 