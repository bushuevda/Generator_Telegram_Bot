# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий запросы к таблице Anecdote."""

#запрос создание таблицы Anecdote
query_create = """
    CREATE TABLE Anecdote
    (id_anecdote INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    text_anecdote TEXT NOT NULL UNIQUE);
"""
#запрос добавления в таблицу Anecdote
query_insert = "INSERT INTO Anecdote(text_anecdote) VALUES(?);" 

#запрос выборки всех записей из таблицы Anecdote
query_select_all = "SELECT * FROM Anecdote;"

#запрос выборки анекдота по id из таблицы Anecdote
query_select_anecdot_on_id = "SELECT text_anecdote FROM Anecdote WHERE id_anecdote = ?;"

#запрос выборки id последней записи в таблице Anecdote
query_last_row = "SELECT id_anecdote FROM Anecdote ORDER BY id_anecdote DESC LIMIT 1;"
