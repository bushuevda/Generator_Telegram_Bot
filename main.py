"""! @brief Главный пакет генератора телеграм бота (точка входа в программу)."""
##
# @mainpage Связи таблицы базы данных
# \image html ./docs/image/database.bmp
##
#
# @section author_doxygen_example Автор
# - Создано Бушуев Дмитрием  24/04/2024 (Created by Bushuev Dmitrii on 24/04/2024).
#
# © Бушуев Д.А., 2024. Все права защищены (Copyright (c) 2024 Bushuev Dmitrii.  All rights reserved).

import asyncio
import logging
from aiogram.enums.parse_mode import ParseMode
from aiogram import Bot
from config import BOT_TOKEN, dp, NAME_DB
from generator_bot import GeneratorBot
import sys

async def main():
    """! Функция запуска бота

        @param bot - Объект класса Bot
    """
    bot = Bot(token = BOT_TOKEN, parse_mode=ParseMode.HTML)
    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot, allowed_updates = dp.resolve_used_update_types())
    

if __name__ == "__main__":
    if len(sys.argv)  >= 2:
        if sys.argv[1] == "new_db":
            if sys.argv[2][-3:] == "dbo":
                from database.create_db import CreateDataBase
                database = CreateDataBase(NAME_DB)
                database.create_tables()
                database.insert_data_to_tables()
            else:
                print('Необходимо ввести название с расширением .dbo!')
        else:
            print('Неверная команда!')
            print('Допустимые команды: \n\t python main.py - запуск приложения\n\t python main.py new_db db_name.dbo - создание базы данных')
        
    elif len(sys.argv) == 1:
        if NAME_DB and BOT_TOKEN:
            a = GeneratorBot(NAME_DB)
            a.generation()
            logging.basicConfig(level = logging.INFO)
            asyncio.run(main())
        else:
            print('NAME_DB или BOT_TOKEN не заполнены!')