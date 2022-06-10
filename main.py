import os
from dotenv import load_dotenv
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


load_dotenv()
TOKEN = os.getenv("TOKEN")


def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot)

    @dp.message_handler()
    async def echo_send(message: types.Message):
        await message.answer(message.text)
        # await message.reply(message.text)
        # await bot.send_message(message.from_user.id, message.text)

    # exchange to 'start_webhook' then you will deploy this repo to the remote hosting
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
