from aiogram import F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, WebAppInfo, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from create_bot import my_router, bot
# from mysql_get import print_rate
from keyboards import builder, builder_inline
# from logger import logger


@my_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    # webappbutton = KeyboardButton(text='WEBAPP BUTTON', web_app=WebAppInfo(url="https://taplink.cc/vnd"))
    builder2 = ReplyKeyboardBuilder()
    # builder2.add(webappbutton)
    await message.answer(f"Hello, {message.from_user.full_name}!", reply_markup=builder2.as_markup())
    await message.delete()


@my_router.message(Command('kb'))
async def message_handler_command_kb(message: Message):
    await message.answer('.' ,reply_markup=builder.as_markup())
    await message.delete()


@my_router.callback_query(F.data == 'pic')
async def callback_query_picture(call):
    await call.message.answer_photo("https://downloader.disk.yandex.ru/preview/3ce8fff9f2add0fcf7ba82db827102b192c678d508a1387d1c791411abbb139e/650bffc8/C_xgAb0IJNQ971p-5C0cD5mX8CU52JCffu0wkN40qmllbQHW_MwBRBzdNRQ3XbAGCiiD7XBDS8rfAng6QImYyQ%3D%3D?uid=0&filename=photo_2023-09-18%2016.00.30.jpeg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")
    await call.message.delete()
    logger.info("command pic pressed")

@my_router.message(F.text == 'inline buttons')
async def message_handler_inline_kb(message: Message):
    await message.answer('choose', reply_markup=builder_inline.as_markup())
    await message.delete()
    logger.info("command inline pressed")

from aiogram import types
@my_router.message(F.text == 'clear')
async def delete_all_messages(chat_id):
    # async for message in types.chat.get_history(chat_id):
    async for message in bot.iter_history(chat_id):
        await message.delete()

@my_router.message(F.text == 'all')
async def get_all_messages_id(chat_id: int):
    messages = []
    async for message in bot.get_chat_history(chat_id):
        messages.append(message.message_id)
    await message.answer(messages)
    return messages
    


@my_router.message(F.text == 'info')
async def message_handler_info(message: Message):
    await message.answer('Location: 🇪🇬 Egypt, Cairo')
    await message.answer('Date: 13/12/2023')
    await message.answer('id: 745005351')
    await message.answer('Melbet ✅')
    # await message.delete()

import random
import time

my_dict1 = ['New game: 1.86x','New game: 15.31x','New game: 12.12x','New game: 9.92x','New game: 3.63x','New game: 16.03x','New game: 34.57x','New game: 11.66x','New game: 22.01x']

my_dict = ['🔸 4.45x 🔸','🔺 19.83 🔺','🔹 1.75 🔹']


random_value = random.choice(my_dict)
print(random_value)


# @my_router.message(F.text == 'GET SIGNAL')
# async def message_get_rate(message: Message):
#     await message.answer(random.choice(my_dict))
#     await message.answer('WAITING!')
#     time.sleep(5)
#     await message.answer('Click get signal to get coefficient for the next round:')
#     await message.delete()
i = 0

@my_router.message(F.text == 'GET SIGNAL')
async def message_get_rate(message: Message):
    global i
    # types.chat.Chat.delete_message(*, dddd)
    # await mess1.delete()
    # await mess2.delete()
    # mess222 = await message.answer(random.choice(my_dict))
    waiting_message = await message.answer('WAITING ⏰')
    await waiting_message.edit_text('WAITING 🟢')
    # time.sleep(1)
    await waiting_message.edit_text('WAITING 🟢🟢')
    # time.sleep(1)
    await waiting_message.edit_text('WAITING 🟢🟢🟢')
    await waiting_message.edit_text('WAITING 🟢🟢🟢🟢')
    await waiting_message.edit_text('WAITING 🟢🟢🟢🟢🟢')
    # await waiting_message.edit_text('WAITING 🟢🟢🟢🟢🟢🟢')
    # await waiting_message.edit_text('WAITING 🟢🟢🟢🟢🟢🟢🟢')
    # await waiting_message.edit_text('WAITING 🟢🟢🟢🟢🟢🟢🟢🟢')
    # await waiting_message.edit_text('WAITING 🟢🟢🟢🟢🟢🟢🟢🟢🟢')
    time.sleep(1)
    await waiting_message.delete()
    mess1 = await message.answer(my_dict[i])
    i += 1
    if i == len(my_dict):
        i = 0
    mess2 = await message.answer('Click get signal to get coefficient for the next round ->')


@my_router.message(F.text.lower().contains('спасибо'))
async def message_handler_mersi(message: Message):
    # await message.answer_animation('CgACAgQAAxkBAAIC9GUEaho8UstXBCHQlhiJCC9DmzBGAAKLAAM_lQRQoW5y7xikiDUwBA')
    await message.reply_animation('CgACAgQAAxkBAAIC9GUEaho8UstXBCHQlhiJCC9DmzBGAAKLAAM_lQRQoW5y7xikiDUwBA')
    logger.info(f"command thanx pressed")




# from create_bot import bot
# @my_router.message(F.text == 'qqq')
# async def message_get_rate(message: Message):
#     global previous_message_id
#     await bot.delete_message(chat_id=message.chat.id, message_id=previous_message_id)
#     await message.answer('qqq pressed')
#     await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
#     # await message.delete()
#     previous_message_id = message.message_id
#     logger.info(f"command qqq pressed")
#     return previous_message_id


# @my_router.message(F.text == 'www')
# async def message_get_rate(message: Message):
#     await message.answer('www pressed')
#     await message.delete()
#     previous_message_id = message.message_id
#     logger.info(f"command www pressed")
#     print(previous_message_id)
#     await bot.delete_message(chat_id=message.chat.id, message_id=2504)

#     return previous_message_id