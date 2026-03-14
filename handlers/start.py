from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Hello! I am your Math Bot.\n\n"
        "Commands:\n"
        "/solve equation\n"
        "/derivative expression\n"
        "/integral expression\n"
        "/matrix operation\n"
        "/plot expression"
    )