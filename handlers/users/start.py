from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import chat
import sqlite3
from keyboards.inline.subscription import sub
from data.config import CHANNELS, ADMINS
from utils.misc import subscription
from loader import dp, bot, db

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.create_table_users()
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        print(f'Xatolik {err}')
    # Проверяем статус подписки пользователя
    is_subscribed = await subscription.check(user_id=message.from_user.id, channel=CHANNELS[0])  # Здесь предполагается, что вы проверяете подписку на первый канал из списка

    if not is_subscribed:
        # Если пользователь еще не подписан, отправляем сообщение с приглашением
        channels_format = str()
        for channel in CHANNELS:
            chat = await bot.get_chat(channel)
            invite_link = await chat.export_invite_link()
            channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"

        await message.answer(f"Quyidagi kanallarga obuna bo'ling: \n"
                             f"{channels_format}",
                             reply_markup=sub,
                             disable_web_page_preview=True)
    else:
        # Если пользователь уже подписан, отправляем другое сообщение или ничего не отправляем
        await message.answer(f"Assalomu alaykum <b>{message.from_user.full_name}</b> bu botdan\n"
                             f" siz <i>TikTokdan video ko'chira olasiz</i> ", disable_web_page_preview=True)

@dp.callback_query_handler(text='check')
async def check_callback_query(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id, channel=channel)

        channel = await bot.get_chat(channel)
        if status:
            result += f"<b>{channel.title}</b> kanaliga obuna bo'lgansiz\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"<b>{channel.title}</b> kanaliga obuna bo'lmagansiz.\n"
                       f"<a href='{invite_link}'>Obuna bo'ling </a>")

    await call.message.answer(result, disable_web_page_preview=True)
