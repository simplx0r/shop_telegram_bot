"""
    Структура клавиатуры отмены
"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def generateBoard (btns: list[str]):
    keyboard = [[]]
    for btn in btns:
        keyboard[0].append(btn)
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


MENU_BOARD = generateBoard(['Развернуть Altrp на сервер'])
