from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

adminbtn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Barcha foydalanuvchilar👤', callback_data='allusers')
        ],
        [
            InlineKeyboardButton(text='Reklama yuborish📝', callback_data='adsend')
        ],
        [
            InlineKeyboardButton(text='Bazani tozalash🔁', callback_data='cleandata')
        ]
    ]
)