# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий класс GetFromDataBase."""

from .tables import*
from aiogram.types import InlineKeyboardButton, KeyboardButton

class GetFromDataBase:
    """! Класс получения информации из базы данных.
    """
    def __init__(self, name_db: str) -> None:
        ## Флаг для формирования списка кнопок
        self.state = False
        ## Объект класса Button
        self.table_button = Button(name_db)
        ## Объект класса CategoryUsers
        self.table_category_user = CategoryUsers(name_db)
        ## Объект класса Inforamtion
        self.table_information = Inforamtion(name_db)
        ## Объект класса KeyWord
        self.table_key_word = KeyWord(name_db)
        ## Объект класса ListButtons
        self.table_list_buttons = ListButtons(name_db)
        ## Объект класса ListInformation
        self.table_list_information = ListInformation(name_db)
        ## Объект класса ListKeyWords
        self.table_list_key_words = ListKeyWords(name_db)
        ## Объект класса ListUsers
        self.table_list_user = ListUsers(name_db)
        ## Объект класса ListVoidMenu
        self.table_list_void_menu = ListVoidMenu(name_db)
        ## Объект класса Menu
        self.table_menu = Menu(name_db)
        ## Объект класса Template
        self.table_template = Template(name_db)
        ## Объект класса TypeInformation
        self.table_type_information = TypeInformation(name_db)
        ## Объект класса User
        self.table_user = User(name_db)
        ## Объект класса TypeMenu
        self.table_type_menu = TypeMenu(name_db)
        ## Объект класса Anecdote
        self.table_anecdote = Anecdote(name_db)

    def get_list_keyboards_reply(self, data_menu_reply: list[list]) -> list[str]:
        """! Функция получения списка линий кнопок для меню reply.

        @param data_meny_reply - данные меню reply.

        Переменные:
            1. list_line_buttons - список линий кнопок.
            2. line_buttons - линия кнопок.
            3. data[1] - название меню.
        
        @return list_line_buttons - возвращает список линий кнопок.    
        """
        list_line_buttons = []
        line_buttons = []
        for data in data_menu_reply:
            line_buttons.append(KeyboardButton(text = data[1]))
            list_line_buttons.append(line_buttons.copy())
            line_buttons.clear()
        return list_line_buttons
    
    def get_list_keyboards_inline(self, name_menu: str) -> list[str]:
        """! Функция получения списка линий кнопок для меню inline.

        @param name_menu - имя меню для которого происходит формирование кнопок.

        Переменные:
            1. name_buttons - название кнопок.
            2. callback_buttons - список callback информации кнопок.
            3. counts_buttons - количество кнопок в ряду(логика построения кнопок).
            4. line_buttons - линия кнопок.
            5. list_line_buttons - список линий кнопок.
        
        Условия:

        1. Если count == 1 и self.state == False, тогда:
            - В список line_buttons добавляется кнопка inline.
            - В список list_line_buttons копируется список line_buttons.
            - Список line_buttons очищается.
        2. Если count == 2 и self.state == False, тогда:
            - В список line_buttons добавляется кнопка inline.
            - self.state = True.
        3. Если self.state == True, тогда:
            - В список line_buttons добавляется кнопка inline:
            - В список list_line_buttons копируется список line_buttons.
            - self.state = True.
            - Список line_buttons очищается.

        @return list_line_buttons - возвращает список линий кнопок.
        """
        name_buttons, callback_buttons, count_buttons = self.table_button.select_on_menu_name(name_menu)
        line_buttons = []
        list_line_buttons = []
        for count, name, callback in zip(count_buttons, name_buttons, callback_buttons):
            if count == 1 and self.state == False:
                line_buttons.append(InlineKeyboardButton(text = name, callback_data = callback))
                list_line_buttons.append(line_buttons.copy())
                line_buttons.clear()
            elif count == 2 and self.state == False:
                line_buttons.append(InlineKeyboardButton(text = name, callback_data = callback))
                self.state = True
            elif self.state:
                line_buttons.append(InlineKeyboardButton(text = name, callback_data = callback))
                list_line_buttons.append(line_buttons.copy())
                self.state = False
                line_buttons.clear()
        self.state = False
        return list_line_buttons
    
    def get_key_words(self, name_menu: str) -> set:
        """! Функция получения ключевых слов для меню.

        @param name_menu - название меню.

        Переменные:
            1. key_words - список ключевых слов для меню.
            2. set_key_words - множество ключевых слов для меню.

        @return set_key_words - множество ключевых слов для меню.
        """
        key_words = self.table_key_word.select_on_menu_name(name_menu) #Select 2
        set_key_words = set()
        for k in key_words:
            set_key_words.add(k) 
        return set_key_words

    def get_list_path_images(self, name_menu: str) -> list[str]:
        """! Функция получения списка путей к изображениям для меню.

        @param name_menu - название меню.

        @return Список путей к изображениям для меню.
        """
        return self.table_information.select_on_menu_name_image(name_menu = name_menu, mod_all = True)

    def get_list_text(self, name_menu: str) -> list[str]:
        """! Функция получения списка теста для меню.
        
        @param name_menu - название меню.

        @return Список текста для меню.
        """
        return self.table_information.select_on_menu_name_text(name_menu = name_menu, mod_all = True)

    def get_text(self, name_menu: str) -> str:
        """! Функция получения теста для меню.
        
        @param name_menu - название меню.

        @return Текст для меню.
        """
        return self.table_information.select_on_menu_name_text(name_menu = name_menu)

    def get_path_file(self, name_menu: str) -> str:
        """! Функция получения пути к файлу для меню.
        
        @param name_menu - название меню.

        @return Путь к файлу для меню.
        """
        return self.table_information.select_on_menu_name_file(name_menu = name_menu)

    def get_path_image(self, name_menu: str) -> str:
        """! Функция получения пути к изображению для меню.
        
        @param name_menu - название меню.

        @return Путь к изображению для меню.
        """
        return self.table_information.select_on_menu_name_image(name_menu = name_menu)

    def get_users(self) -> dict:
        """! Функция получения словаря пользователей.
        
        @param name_menu - название меню.

        @return Словарь пользователей.
        """
        return self.table_user.select_on_parser()

    def get_function_anecdot(self) -> object:
        """! Функция возвращающая функцию получения анекдота по id анекдоту.

        @return Текст анекдота.
        """
        return self.table_anecdote.select_anecdote_on_id
    
    def get_len_list_anecdotes(self) -> int:
        """! Функция получения количества анектодов в базе данных.

        @return Количество анектодов в базе данных.
        """
        return self.table_anecdote.get_last_row()