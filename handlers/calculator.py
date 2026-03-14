from aiogram import Router
from aiogram.types import Message
from sympy import latex
from services.math_solver import solve_expression

router = Router()

@router.message()
async def calculate(message: Message):
    # Skip commands
    if message.text.startswith("/"):
        return

    try:
        result = solve_expression(message.text)
        await message.answer(f"<b>Result:</b>\n<code>{latex(result)}</code>", parse_mode="HTML")
    except Exception:
        await message.answer("Invalid expression")