# services/ai_helper.py
from google.genai import Client
from config import AI_TOKEN

client = Client(api_key=AI_TOKEN)


SYSTEM_PROMPT = """
You are a math solving assistant.

Rules:
- Give clear step-by-step solutions.
- Keep explanations short.
- Write formulas in simple readable math format.
- Do NOT use LaTeX like \\frac or \\left.
- Write expressions like: sqrt(3)/4, x^2, etc.
- Always show the final answer clearly.
"""


def ask_ai(prompt: str) -> str:
    """
    Send question to Gemini and return formatted answer.
    """

    full_prompt = f"{SYSTEM_PROMPT}\n\nProblem:\n{prompt}"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )

    return response.text