from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.reply("Здраствуй, обычный пользователь!")


@user_router.message(Command("help"))
async def user_help(message: Message):

    m = "Привет, я бот помощник для ClientMod!\n"
    m += "Команды:\n\n"
    m += "/cm - получить последнюю версию клиентмода.\n"
    m += "/cn - получить последнюю версию движка для клиентмода.\n\n"
    m += "ClientMod | CustomEngine by AndraMidoxXx"

    await message.reply(m)


@user_router.message(Command("cm"))
async def user_cm(message: Message):

    m = "https://t.me/Sayuuuu_topp/455\n\n"
    m += "Не забудь подписаться на @Sayuuuu_topp, "
    m += "если ещё не подписан."

    await message.reply(m)


@user_router.message(Command("cn"))
async def user_cn(message: Message):

    m = "https://t.me/Sayuuuu_topp/456\n\n"
    m += "Не забудь подписаться на @Sayuuuu_topp, "
    m += "если ещё не подписан."

    await message.reply(m)