import asyncio
import json
from loader import types, dp, bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Filter, Text
from data.TikTokApi import get_tiktok_data

class LinkFilter(Filter):
    async def check(self, message: types.Message) -> bool:
        return message.text.startswith('http')

@dp.message_handler(LinkFilter())
async def link_handler(message: types.Message):
    link = message.text
    msg = await message.answer("<i>Sizning so'rovingizni ko'rib chiqayapmiz kuting😉!</i>")
    video_link = None  # Initialize with a default value

    try:
        data1 = get_tiktok_data(link)
        music_link = data1['music']  # Convert to a JSON string
        video_link = data1['video']
    except Exception as e:
        print(f"Xatolik: {e}")
    try:
        btn = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='🎵Musiqani yuklab olish', url=music_link)
                ]
            ]
        )
    except UnboundLocalError as a:
        pass
    if video_link:
        await msg.edit_text('⏳')
        await asyncio.sleep(5)
        await msg.delete()
        await message.answer_video(video_link, caption='Done', reply_markup=btn)
    else:
        await msg.edit_text("<b>Men faqat TikTok havolalarni o'qiy olama</b>❌")


