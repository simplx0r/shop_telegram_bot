#  Copyright (c) 2022.

from aiogram import F
from aiogram import Router
from aiogram.filters import Command
from aiogram.filters.command import CommandStart
from aiogram.fsm.state import any_state
from aiogram.types import ContentType
from aiogram.utils.i18n import lazy_gettext as __

from bot.handlers.create_post import menu_posts_create, menu_posts_create_text, menu_posts_create_url, \
    menu_posts_create_prtype, menu_posts_create_prtype_url, menu_posts_create_prtype_pub, menu_posts_create_subs_min
from bot.handlers.get_post import menu_posts_get
from bot.handlers.help import help_command, help_func, call_help_func
from bot.handlers.start import (
    start,
    menu_posts,
    menu_account,
    menu_channels,
    PostStates, call_start
)
from bot.structures.callback_data_factories import PostCD, PostCDAction

__all__ = ('register_user_commands', 'bot_commands', 'register_user_handlers',)


def register_user_commands(router: Router) -> None:
    """
    Зарегистрировать хендлеры пользователя
    :param router:
    """
    router.message.register(start, CommandStart())

    router.message.register(start, F.text == __('Старт'))
    router.message.register(menu_posts, F.text == __('Твои посты'))
    router.message.register(menu_account, F.text == __('Аккаунт'), F.content_type == [ContentType.CONTACT, ])
    router.message.register(menu_channels, F.text == __('Твои каналы'))






# Alias
register_user_handlers = register_user_commands
