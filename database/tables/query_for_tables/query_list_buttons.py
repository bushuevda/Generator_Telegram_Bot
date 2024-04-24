# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий запросы к таблице List_Buttons."""

#запрос создание таблицы List_Buttons
query_create = """
    CREATE TABLE List_Buttons
    (id_list_buttons INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    id_menu INTEGER NOT NULL,
    id_button INTEGER NOT NULL,
    FOREIGN KEY (id_button) REFERENCES Button(id_button),
    FOREIGN KEY (id_menu) REFERENCES Menu(id_menu));
"""

#запрос добавления в таблицу List_Buttons
query_insert = "INSERT INTO List_Buttons (id_menu, id_button) VALUES(?, ?);" 