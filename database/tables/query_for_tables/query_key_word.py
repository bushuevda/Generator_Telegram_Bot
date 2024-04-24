# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий запросы к таблице Key_Word."""

#запрос создание таблицы Key_Word
query_create = """
    CREATE TABLE Key_Word
    (id_key_word INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL,
    word TEXT NOT NULL UNIQUE);
"""

#запрос добавления в таблицу Key_Word
query_insert = "INSERT INTO Key_Word (word) VALUES(?);" 

#запрос выборки записей из таблицы Key_word по название меню
query_on_menu_name = """
  SELECT word FROM Key_Word 
  INNER JOIN List_Key_Words 
  ON List_Key_Words.id_key_word = Key_Word.id_key_word
  INNER JOIN Menu
  ON Menu.id_menu = List_Key_Words.id_Menu
  WHERE Menu.name_menu = ?;
"""