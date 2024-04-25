# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).
"""! @brief Пакет содержащий класс GeneratorBot."""

from database import*
from inline_menu import*
from answer import*
from reply_menu import*
from config import password_registration, WELCOME_MESSAGE

class GeneratorBot:
    """! Класс генерации данных бота
    """
    def __init__(self, name_db: str) -> None:
        ## Объект класса GetFromDataBase
        self.get_from_database = GetFromDataBase(name_db = name_db)
        ## Объект класса ManagerUsers
        self.manager_users = ManagerUsers(dict_users = self.get_from_database.get_users(), name_db = name_db)
        ## Объект класса AnswerEditPhoto
        self.answer_edit_photo = AnswerEditPhoto(manager_users = self.manager_users)
        ## Объект класса AnswerEditText
        self.answer_edit_text = AnswerEditText(manager_users = self.manager_users)
        ## Объект класса AnswerFile
        self.answer_file = AnswerFile(manager_users = self.manager_users)
        ## Объект класса AnswerPhoto
        self.answer_photo = AnswerPhoto(manager_users = self.manager_users)
        ## Объект класса AnswerText
        self.answer_text = AnswerText(manager_users = self.manager_users)
        ## Объект класса AnswerBackImage
        self.answer_back_image = AnswerBackImage(manager_users = self.manager_users)
        ## Объект класса AnswerForwardImage
        self.answer_forward_image = AnswerForwardImage(manager_users = self.manager_users)
        ## Объект класса InlineAnecdote
        self.inline_anecdote = InlineAnecdote(manager_users = self.manager_users, 
                                              len_list_anecdotes = self.get_from_database.get_len_list_anecdotes())
        ## Объект класса InlinePhoto
        self.inline_photo = InlinePhoto(manager_users = self.manager_users)
        ## Объект класса InlineText
        self.inline_text = InlineText(manager_users = self.manager_users)
        ## Объект класса InlineFile
        self.inline_file = InlineFile(manager_users = self.manager_users)
        ## Объект класса ReplyMenu
        self.reply_menu = ReplyMenu(answer_message = WELCOME_MESSAGE,
                                     command="start", manager_users = self.manager_users,
                                     registration_password = password_registration)
        
    def generation_reply(self) -> None:
        """! Функция генерации меню reply.

            Переменные:
                1. data_menu_reply - информация о меню reply.
                2. keyboard - список кнопок меню.
        """
        data_menu_reply = self.get_from_database.table_menu.select_menu_on_type(1)
        keyboard = self.get_from_database.get_list_keyboards_reply(data_menu_reply = data_menu_reply) 
        self.reply_menu.create(keyboard = keyboard)
        self.reply_menu.admin()      
        self.reply_menu.registration()  

    def generation_inline(self) -> None:
        """! Функция генерации меню inline.

            Переменные:
                1. data_menu_inline - информация о меню inline.
                2. menu[1] - name_menu из таблицы Menu.
                3. menu[2] - id_template из таблицы Menu.
                4. key_words - список ключевых слов для меню.
                5. keyboard - список кнопок меню.
                6. text - текст для меню.
                7. path_image - путь к изображению.
                8. caption - описание изображения или файла.
                9. file_path - путь к файлу.
            
            Условия:
                1. Если menu[2] == 1 то генерируется меню inline с шаблоном 'Текст'.
                2. Если menu[2] == 2 то генерируется меню inline с шаблоном 'Текст с картинкой'.
                3. Если menu[2] == 5 то генерируется меню inline с шаблоном 'Текст с файлом'.
        """
        data_menu_inline = self.get_from_database.table_menu.select_all()
        for menu in data_menu_inline:
            name_menu = menu[1]
            key_words = self.get_from_database.get_key_words(name_menu = menu[1])
            keyboard = self.get_from_database.get_list_keyboards_inline(name_menu = menu[1])

            if menu[2] == 1:
                text = self.get_from_database.get_text(name_menu = menu[1])
                if text == " ":
                    text = name_menu
                self.inline_text.create(name_menu = name_menu, keyboard = keyboard, text = text, key_words = key_words)

            elif menu[2] == 2:
                path_image = self.get_from_database.get_path_image(name_menu = menu[1])
                caption = self.get_from_database.get_text(name_menu = menu[1])
                self.inline_photo.create(name_menu = name_menu, key_words = key_words, path_image = path_image, 
                                         keyboard = keyboard, caption = caption)
                
            elif menu[2] == 5:
                file_path = self.get_from_database.get_path_file(name_menu = menu[1])
                caption = self.get_from_database.get_text(name_menu = menu[1])
                self.inline_file.create(name_menu = menu[1], key_words = key_words, file_path = file_path,
                                         keyboard = keyboard, caption = caption)

        self.inline_anecdote.create(self.get_from_database.get_function_anecdot)
  
    def generation_answer_event(self) -> None:
        """! Функция генерации событий для кнопок.

            Переменные:
                1. all_rows_button_inline - данные кнопок inline.
                2. data_menu_inline - информация о меню inline.
                3. keyboard - список кнопок меню.
                4. path_image - путь к изображению.
                5. caption - описание изображения.

            Условия:
                1. Если button[4] == 2 создается событие переключения изображения назад для заданной кнопки.
                2. Если button[4] == 3 создается событие переключения изображения вперед для заданной кнопки.
        """
        all_rows_button_inline = self.get_from_database.table_button.select_all()
        for button in all_rows_button_inline:
            data_menu_inline = self.get_from_database.table_menu.select_menu_on_id_button(id_button = button[0])
            if len(data_menu_inline) >= 1:
                for menu in data_menu_inline:
                    keyboard = self.get_from_database.get_list_keyboards_inline(menu[0])  
                    path_image = self.get_from_database.get_list_path_images(menu[0])
                    caption = self.get_from_database.get_list_text(menu[0])

                    if button[4] == 2:
                        self.answer_forward_image.create(cb_data = button[2], path_images = path_image, 
                                                         keyboard = keyboard, captions = caption)
                    elif button[4] == 3:
                        self.answer_back_image.create(cb_data = button[2], path_images = path_image, 
                                                      keyboard = keyboard, captions = caption)       

    def generation_answer_menu(self) -> None:
        """! Функция генерации меню answer.

            Переменные:
                1. all_rows_button_answer - данные кнопок inline.
                2. data_menu_inline - информация о меню answer.
                3. keyboard - список кнопок меню.
                4. path_image - путь к изображению.
                5. caption - описание изображения.
                6. menu[0] - name_menu из таблицы Menu.
                7. menu[1] - id_template из таблицы Menu.
                8. button[2] - callback_data из таблицы Button.
                
            Условия:
                1. menu[1] == 1 создается меню inline с шаблоном 'Текст'.
                2. menu[1] == 2 создается меню inline с шаблоном 'Текст с картинкой'.
                3. menu[1] == 3 создается меню inline с шаблоном 'Изменение текста с картинкой'.
                4. menu[1] == 4 создается меню inline с шаблоном 'Изменение текста'.
                5. menu[1] == 5 создается меню inline с шаблоном 'Текст с файлом'.
        """        
        all_rows_button_inline = self.get_from_database.table_button.select_all()
        for button in all_rows_button_inline:
            data_menu_inline = self.get_from_database.table_menu.select_menu_on_callback(cb_data = button[2])
            if len(data_menu_inline) >= 1:
                for menu in data_menu_inline:
                    keyboard = self.get_from_database.get_list_keyboards_inline(menu[0])  

                    if menu[1] == 1:
                        text = self.get_from_database.get_text(name_menu = menu[0])
                        if text == " ":
                            text = menu[0]
                        self.answer_text.create(cb_data = button[2], keyboard = keyboard, text = text)
                    
                    elif menu[1] == 2:
                        path_image = self.get_from_database.get_path_image(name_menu = menu[0])
                        caption = self.get_from_database.get_text(name_menu = menu[0])
                        self.answer_photo.create(cb_data = button[2], path_image = path_image, 
                                                 keyboard = keyboard, caption = caption)

                    elif menu[1] == 3:
                        list_path_image = self.get_from_database.get_list_path_images(name_menu = menu[0])
                        list_caption = self.get_from_database.get_list_text(name_menu = menu[0])
                        self.answer_edit_photo.create(cb_data = button[2], list_path_image = list_path_image, 
                                                      keyboard = keyboard, list_caption = list_caption)
                    
                    elif menu[1] == 4:
                        text = self.get_from_database.get_text(name_menu = menu[0])
                        if text == " ":
                            text = menu[0]
                        self.answer_edit_text.create(cb_data = button[2], keyboard = keyboard, text = text)
             
                    elif menu[1] == 5:
                        file_path = self.get_from_database.get_path_file(name_menu = menu[0])
                        caption = self.get_from_database.get_text(name_menu = menu[0])
                        self.answer_file.create(cb_data = button[2], file_path = file_path, 
                                                keyboard = keyboard, caption = caption)

    def generation(self) -> None:
        """! Функция генерации бота.
        """
        self.generation_reply()
        self.generation_inline()
        self.generation_answer_menu()
        self.generation_answer_event()