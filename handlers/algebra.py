from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from sympy import latex
from services.math_solver import solve_equation, derivative, integral

router = Router()

@router.message(Command("solve"))
async def solve_cmd(message: Message):
    expr = message.text.replace("/solve", "").strip()
    try:
        result = solve_equation(expr)
        # Use LaTeX for equations
        await message.answer(f"<b>Solutions:</b>\n<code>{latex(result)}</code>", parse_mode="HTML")
    except Exception as e:
        await message.answer(f"Invalid equation: {e}")


@router.message(Command("derivative"))
async def derivative_cmd(message: Message):
    expr = message.text.replace("/derivative", "").strip()
    try:
        result = derivative(expr)
        await message.answer(f"<b>Derivative:</b>\n<code>{latex(result)}</code>", parse_mode="HTML")
    except Exception as e:
        await message.answer(f"Invalid expression: {e}")


@router.message(Command("integral"))
async def integral_cmd(message: Message):
    expr = message.text.replace("/integral", "").strip()
    try:
        result = integral(expr)
        await message.answer(f"<b>Integral:</b>\n<code>{latex(result)} + C</code>", parse_mode="HTML")
    except Exception as e:
        await message.answer(f"Invalid expression: {e}")