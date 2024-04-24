# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий класс CreateDataBase."""

from .tables import*

class CreateDataBase:
    """! Класс создания базы даных.
    """
    def __init__(self, name_db: str) -> None:
        ## Имя базы данных
        self.name_db = name_db
        ## Объект таблицы Button
        self.button = Button(self.name_db)
        ## Объект таблицы CategoryUsers
        self.category_users = CategoryUsers(self.name_db)
        ## Объект таблицы Inforamtion
        self.information = Inforamtion(self.name_db)
        ## Объект таблицы KeyWord
        self.key_word = KeyWord(self.name_db)
        ## Объект таблицы ListButtons
        self.list_buttons = ListButtons(self.name_db)
        ## Объект таблицы ListInformation
        self.list_information = ListInformation(self.name_db)
        ## Объект таблицы ListKeyWords
        self.list_key_words = ListKeyWords(self.name_db)
        ## Объект таблицы ListUsers
        self.list_users = ListUsers(self.name_db)
        ## Объект таблицы ListVoidMenu
        self.list_void_menu = ListVoidMenu(self.name_db)
        ## Объект таблицы Menu
        self.menu = Menu(self.name_db)
        ## Объект таблицы Template
        self.template = Template(self.name_db)
        ## Объект таблицы User
        self.user = User(self.name_db)
        ## Объект таблицы TypeMenu
        self.type_menu = TypeMenu(self.name_db)
        ## Объект таблицы TypeInformation
        self.type_information = TypeInformation(self.name_db)
        ## Объект таблицы Event
        self.event = Event(self.name_db)
        ## Объект таблицы Anecdote
        self.anecdote = Anecdote(self.name_db)

    def create_tables(self) -> None:
        """! Функция создания таблиц базы данных.
        """
        self.button.create()
        self.category_users.create()
        self.information.create()
        self.key_word.create()
        self.list_buttons.create()
        self.list_information.create()
        self.list_key_words.create()
        self.list_users.create()
        self.list_void_menu.create()
        self.menu.create()
        self.template.create()
        self.user.create()
        self.type_menu.create()
        self.type_information.create()
        self.event.create()
        self.anecdote.create()

    def insert_data_to_tables(self) -> None:
        """! Функция добавления информации в базу данных.
        """
        self.button.insert_data()
        self.category_users.insert_data()
        self.information.insert_data()
        self.key_word.insert_data()
        self.list_buttons.insert_data()
        self.list_information.insert_data()
        self.list_key_words.insert_data()
        self.list_void_menu.insert_data()
        self.menu.insert_data()
        self.template.insert_data()
        self.type_menu.insert_data()
        self.type_information.insert_data()
        self.event.insert_data()
        self.anecdote.insert_data()
        

 