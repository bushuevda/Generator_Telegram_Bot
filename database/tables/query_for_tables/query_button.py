# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий запросы к таблице Button."""

#запрос создание таблицы Button
query_create = """
    CREATE TABLE Button
    (id_button INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    name_button TEXT NOT NULL,
    callback_data TEXT NOT NULL UNIQUE,
    line INT NOT NULL,
    id_event INT NOT NULL,
    FOREIGN KEY (id_event) REFERENCES Event(id_event));
"""
#запрос добавления в таблицу Button
query_insert = "INSERT INTO Button(name_button, callback_data, line, id_event) VALUES(?, ?, ?, ?);" 

#запрос выборки всех записей из таблицы Button
query_select_all = "SELECT * FROM Button;"

#запрос выборки записей из таблицы Button по название меню 
query_on_menu_name = """
    SELECT Button.name_button, Button.callback_data,
    Button.line FROM Button INNER JOIN List_Buttons
    ON List_Buttons.id_button = Button.id_button
    INNER JOIN Menu ON Menu.id_Menu = List_Buttons.id_menu
    WHERE Menu.name_menu = ?;
"""

#запрос выборки записей из таблицы Button по callback_data 
query_on_callback_data = """
    SELECT Button.name_button, Button.callback_data,
    Button.ryd FROM Button INNER JOIN List_Buttons
    ON List_Buttons.id_button = Button.id_button
    INNER JOIN Menu ON Menu.id_menu = List_Buttons.id_menu
    WHERE Menu.id_menu IN 
        (SELECT List_Void_Menu.id_menu FROM List_Void_Menu
        INNER JOIN Button
        ON List_Void_Menu.id_button = Button.id_button
        WHERE Button.callback_data = ?);
"""