# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий запросы к таблице Menu."""

#запрос создание таблицы Menu
query_create = """
    CREATE TABLE Menu
    (id_menu INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    name_menu TEXT NOT NULL UNIQUE,
    id_template INTEGER,
    id_category_users INTEGER,
    id_type_menu INTEGER,
    FOREIGN KEY (id_template) REFERENCES Template(id_template),
    FOREIGN KEY (id_category_users) REFERENCES Category_Users(id_category_users)
    FOREIGN KEY (id_type_menu) REFERENCES Type_Menu(id_type_menu));
"""

#запрос добавления в таблицу Menu
query_insert = "INSERT INTO Menu (name_menu, id_template, id_category_users, id_type_menu) VALUES(?, ?, ?, ?);" 

#запрос выборки всех записей из таблицы Menu
query_select_all = """ SELECT * FROM Menu;"""

#запрос выборки записей из таблицы Menu по типу меню 
query_select_menu_on_type = """SELECT * FROM Menu WHERE id_type_menu = ?;"""

#запрос выборки записей из таблицы Menu по callback_data 
query_select_menu_on_callback = """
    SELECT name_menu, id_template FROM Menu
    INNER JOIN List_Void_Menu 
    ON List_Void_Menu.id_menu = Menu.id_menu
    INNER JOIN Button
    ON List_Void_Menu.id_button = Button.id_button
    WHERE Button.callback_data = ?;
"""

#запрос выборки записей из таблицы Menu по id_button 
query_select_menu_on_id_button = """
    SELECT name_menu, id_template FROM Menu
    INNER JOIN List_Buttons 
    ON List_Buttons.id_menu = Menu.id_menu
    WHERE List_Buttons.id_button = ?;
"""