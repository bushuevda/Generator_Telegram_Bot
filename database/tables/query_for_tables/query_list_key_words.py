# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий запросы к таблице List_Key_Words."""

#запрос создание таблицы List_Key_Words
query_create = """
    CREATE TABLE List_Key_Words
    (id_list_key_words INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    id_menu INTEGER NOT NULL,
    id_key_word INTEGER NOT NULL,
    FOREIGN KEY (id_key_word) REFERENCES Key_Word(id_key_word),
    FOREIGN KEY (id_menu) REFERENCES Menu(id_menu));
"""

#запрос добавления в таблицу List_Key_Words
query_insert = "INSERT INTO List_Key_Words (id_menu, id_key_word) VALUES(?, ?);" 