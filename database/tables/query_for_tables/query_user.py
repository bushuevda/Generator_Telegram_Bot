# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий запросы к таблице User."""

#запрос создание таблицы User
query_create = """
    CREATE TABLE User
    (id_user INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    name_account TEXT NOT NULL,
    id_account INT NOT NULL UNIQUE);
"""

#запрос добавления в таблицу User
query_insert = "INSERT INTO User (name_account, id_account) VALUES(?, ?);" 

query_insert_user_list_users = """
    BEGIN TRANSACTION;
    INSERT INTO User(name_account, id_account) VALUES(?, ?);
    SELECT id_user FROM User ORDER BY id_user DESC LIMIT 1;
    INSERT INTO List_Users(id_user, id_category_users) VALUES ()
    COMMIT;
"""

#запрос выборки всех записей из таблицы User
query_select_all = "SELECT name_account, id_account FROM User;"

#запрос выборки id пользователя из таблицы User по id_account 
query_select_id_user_on_id_account = """SELECT id_user FROM User WHERE id_account = ?;"""

#запрос выборки категории  по id_account 
query_select_category_on_id_account = """
    SELECT Category_Users.name_category
    FROM User INNER JOIN List_Users ON User.id_user = List_Users.id_user
    INNER JOIN Category_Users ON Category_Users.id_category_users = List_Users.id_category_Users
    WHERE User.id_account = ?;
"""

#запрос выборки id последней записи таблицы User
query_last_row = "SELECT id_user FROM User ORDER BY id_user DESC LIMIT 1"

#запрос выборки информации о пользователе из таблицы User по категории
query_select_user_on_category = """
    SELECT User.name_account, User.id_account
    FROM User INNER JOIN List_Users ON User.id_user = List_Users.id_user
    INNER JOIN Category_Users ON Category_Users.id_category_users = List_Users.id_category_Users
    WHERE Category_Users.name_category = ?;
"""