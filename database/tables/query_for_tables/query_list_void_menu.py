# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий запросы к таблице List_Void_Menu."""

#запрос создание таблицы List_Void_Menu
query_create = """
    CREATE TABLE List_Void_Menu
    (id_list_void_menu INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    id_menu INTEGER NOT NULL,
    id_button INTEGER NOT NULL,
    FOREIGN KEY (id_menu) REFERENCES Menu(id_menu),
    FOREIGN KEY (id_button) REFERENCES Button(id_button));
"""

#запрос добавления в таблицу List_Void_Menu
query_insert = "INSERT INTO List_Void_Menu (id_menu, id_button) VALUES(?, ?);" 