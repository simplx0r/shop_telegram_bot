"""
    Файл хендлеров, связанных с командой /start
"""
#  Copyright (c) 2022.

from contextlib import suppress

from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _
from sqlalchemy import select  # type: ignore
from sqlalchemy.orm import sessionmaker, joinedload, selectinload  # type: ignore

from bot.db.user import get_user
from bot.structures.fsm_groups import PostStates
from bot.structures.keyboards import MENU_BOARD
from bot.structures.keyboards.posts_board import generate_posts_board


async def start(message: types.Message) -> Message:
    """
    Хендлер для команды /start
    :param message:
    """
    return await message.answer(_('Swag 228 1337'), reply_markup=MENU_BOARD)


async def call_start(call: types.CallbackQuery, state: FSMContext) -> Message:
    """
    Хендлер для команды /start
    :param call:
    :param state:
    """
    await state.clear()
    with suppress(Exception):
        await call.message.delete()
    return await call.message.answer(_('Swag 228 1337'), reply_markup=MENU_BOARD)




