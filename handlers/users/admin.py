import asyncio

from aiogram import types
from keyboards.inline.foradmins import adminbtn
from data.config import ADMINS
from loader import dp, db, bot


waiting_for_message = {}



@dp.message_handler(commands=['admin'], user_id=ADMINS)
async def admin_panel(message: types.Message):
    await message.answer('ADMIN PANELga xush kelibsiz👇', reply_markup=adminbtn)


@dp.callback_query_handler(text="allusers", user_id=ADMINS)
async def get_all_users(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    users = db.select_all_users()

    # Creating a formatted message for all users
    message_text = "Barcha foydalanuvchilar ro'yhati:\n\n"
    for user in users:
        message_text += f'ID: {user[0]}\nIsmi: {user[1]}\n\n'

    # Sending the entire message outside the loop
    await call.message.answer(message_text)
@dp.callback_query_handler(text='adsend', user_id=ADMINS)
async def send_ad_prompt(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    user_id = call.message.from_user.id
    waiting_for_message[user_id] = True
    await call.bot.send_message(chat_id=call.message.chat.id, text="Xabaringizni yozing:")

@dp.message_handler(lambda call: waiting_for_message.get(call.from_user.id, ADMINS))
async def send_ad_to_all(message: types.Message):
    print("Callback function triggered.")
    user_id = message.from_user.id
    waiting_for_message[user_id] = False
    users = db.select_all_users()
    ad_message = message.text
    print(f"Sending ad message: {ad_message} to all users.")
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text=ad_message)
        await asyncio.sleep(0.05)

@dp.callback_query_handler(text="cleandata", user_id=ADMINS)
async def get_all_users(call: types.CallbackQuery):
    db.delete_users()
    await call.answer(cache_time=60)
    await call.message.answer("Baza tozalandi!")