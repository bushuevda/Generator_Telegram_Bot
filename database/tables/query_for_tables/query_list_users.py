# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий запросы к таблице List_Users."""

#запрос создание таблицы List_Users
query_create = """
    CREATE TABLE List_Users
    (id_list_users INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    id_user INTEGER,
    id_category_users INTEGER,
    FOREIGN KEY (id_category_users) REFERENCES Category_Users(id_category_users),
    FOREIGN KEY (id_user) REFERENCES User(id_user));
"""

#запрос добавления в таблицу List_Users
query_insert = "INSERT INTO List_Users (id_user, id_category_users) VALUES(?, ?);" 

#запрос изменения категории пользователя в таблице List_Users на "Обычный пользователь"
query_update_notban = """UPDATE List_Users SET id_category_users = 1 WHERE id_user = ?;"""

#запрос изменения категории пользователя в таблице List_Users на "Администратор"
query_update_admin = """UPDATE List_Users SET id_category_users = 2 WHERE id_user = ?;"""

#запрос изменения категории пользователя в таблице List_Users на "Черный список"
query_update_ban = """UPDATE List_Users SET id_category_users = 3 WHERE id_user = ?;"""





