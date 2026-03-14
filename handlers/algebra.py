from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from sympy import latex
from services.math_solver import solve_equation, derivative, integral

router = Router()

# --- Solve ---
@router.message(Command("solve"))
async def solve_cmd(message: Message):
    expr = message.text.replace("/solve", "").strip()
    try:
        result = solve_equation(expr)
        # Convert to LaTeX for Telegram
        latex_result = ', '.join([latex(r) for r in result])
        await message.answer(f"<b>Solutions:</b>\n${latex_result}$", parse_mode="HTML")
    except Exception as e:
        await message.answer(f"Invalid equation: {e}")

# --- Derivative ---
@router.message(Command("derivative"))
async def derivative_cmd(message: Message):
    expr = message.text.replace("/derivative", "").strip()
    try:
        result = derivative(expr)
        await message.answer(f"<b>Derivative:</b>\n${latex(result)}$", parse_mode="HTML")
    except Exception as e:
        await message.answer(f"Invalid expression: {e}")

# --- Integral ---
@router.message(Command("integral"))
async def integral_cmd(message: Message):
    expr = message.text.replace("/integral", "").strip()
    try:
        result = integral(expr)
        await message.answer(f"<b>Integral:</b>\n${latex(result)} + C$", parse_mode="HTML")
    except Exception as e:
        await message.answer(f"Invalid expression: {e}")