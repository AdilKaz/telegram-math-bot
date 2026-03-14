from aiogram import Router, types
from services.ai_helper import ask_ai
import re

router = Router()
MAX_LENGTH = 4000


def split_text(text, max_len=4000):
    parts = text.split("\n\n")
    chunks = []
    current = ""

    for part in parts:
        if len(current) + len(part) < max_len:
            current += part + "\n\n"
        else:
            chunks.append(current)
            current = part + "\n\n"

    if current:
        chunks.append(current)

    return chunks

def format_latex_readable(text):
    """Break long LaTeX formulas into smaller readable lines."""
    parts = re.split(r'(\\frac|\\sqrt|\\left|\\right|[+=-])', text)

    lines = []
    line = ""

    for i, part in enumerate(parts):
        line += part
        if (i + 1) % 8 == 0:
            lines.append(line)
            line = ""

    if line:
        lines.append(line)

    return "\n".join(lines)


@router.message()
async def ai_handler(message: types.Message):
    if not message.text.startswith("/ai"):
        return

    query = message.text[3:].strip()

    try:
        response = ask_ai(query)
    except Exception as e:
        await message.answer(f"AI error: {e}")
        return

    # make math more readable
    response = format_latex_readable(response)

    for chunk in split_text(response):

        if any(c in chunk for c in "=+-*/^()√"):
            await message.answer(f"```\n{chunk}\n```", parse_mode="Markdown")
        else:
            await message.answer(chunk)