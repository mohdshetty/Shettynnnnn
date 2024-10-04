import asyncio

from aiogram import Router, Bot, Dispatcher, F
from aiogram.types import Message, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder

from configs.config_reader import Config


def webapp_builder(user_id, username) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(text='Start main with us!', web_app=WebAppInfo(
        url=f"https://99c0-31-40-25-32.ngrok-free.app/start?user_id={user_id}&username={username}",
    ))
    return builder.as_markup()

router = Router()

@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.reply('Привет!',
                        reply_markup=webapp_builder(message.from_user.id, message.from_user.username))
    
async def main() -> None:
    bot = Bot(token=Config.get_config(0, "config_app").TOKEN, parse_mode=ParseMode.HTML)
    
    dp = Dispatcher()
    dp.include_router(router)
    
    await bot.delete_webhook(True)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':

    text = 'Bot started'
    print(f'{text:*^30}')
    asyncio.run(main())

