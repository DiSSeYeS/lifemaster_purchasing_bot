import asyncio

from aiogram import Bot, Dispatcher
from handlers import choosing_handlers, other_handlers, user_handlers, admin_handlers
from states import BOT_TOKEN


# Инициализируем бот и диспетчер
bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()

# Функция конфигурирования и запуска бота
async def main() -> None:

    # Регистрируем роутеры в диспетчере
    dp.include_router(admin_handlers.router)
    dp.include_router(user_handlers.router)
    dp.include_router(choosing_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())