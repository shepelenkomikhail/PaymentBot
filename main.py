from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.types import LabeledPrice
from aiogram.filters import CommandStart
import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot=bot)


@dp.message(CommandStart())
async def start(message: types.Message):
    title = 'Course'
    description = 'Course description'
    invoice_payload = 'invoice'
    currency = 'HUF'
    prices = [LabeledPrice(label='Course', amount=10000 * 100)]

    try:
        await bot.send_invoice(
            chat_id=message.chat.id,
            title=title,
            description=description,
            payload=invoice_payload,
            provider_token=config.STRIPE_TEST_TOKEN,
            currency=currency,
            prices=prices,
        )
    except Exception as e:
        await message.reply(f"Failed to send invoice. Error: {e}")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
