# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий запросы к таблице Information."""

## запрос создание таблицы Information
query_create = """
  CREATE TABLE Information
  (id_information INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
  information TEXT NOT NULL);
"""

#запрос добавления в таблицу Information
query_insert = "INSERT INTO Information (information) VALUES(?);" 

#запрос выборки записей из таблицы Information по название меню с категорией 'Изображение'
query_on_menu_name_image = """
  SELECT Information.information FROM Information
  INNER JOIN List_Information ON List_Information.id_information = Information.id_information
  INNER JOIN Type_Information ON Type_Information.id_type_information = List_Information.id_type_information
  INNER JOIN Menu ON Menu.id_menu = List_Information.id_menu
  WHERE Menu.name_menu = ? AND Type_Information.name_type = 'Изображение';
"""

#запрос выборки записей из таблицы Information по название меню с категорией 'Текст'
query_on_menu_name_text = """
  SELECT Information.information FROM Information
  INNER JOIN List_Information ON List_Information.id_information = Information.id_information
  INNER JOIN Type_Information ON Type_Information.id_type_information = List_Information.id_type_information
  INNER JOIN Menu ON Menu.id_menu = List_Information.id_menu
  WHERE Menu.name_menu = ? AND Type_Information.name_type = 'Текст';
"""

#запрос выборки записей из таблицы Information по название меню с категорией 'Файл'
query_on_menu_name_file = """
  SELECT Information.information FROM Information
  INNER JOIN List_Information ON List_Information.id_information = Information.id_information
  INNER JOIN Type_Information ON Type_Information.id_type_information = List_Information.id_type_information
  INNER JOIN Menu ON Menu.id_menu = List_Information.id_menu
  WHERE Menu.name_menu = ? AND Type_Information.name_type = 'Файл';
"""