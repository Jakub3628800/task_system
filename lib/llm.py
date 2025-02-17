from litellm import completion


MODELS = {
        "claude": "anthropic/claude-3-5-sonnet-20241022",
        "deepseek": "deepseek/deepseek-chat",
        "r1": "deepseek/deepseek-reasoner"
        }

def respond(message: str, model: str = "r1") -> str:
    response = completion(
        model=MODELS[model],
        messages=[{ "content": message, "role": "user"}]
    )
    return response.choices[0].message.content


SUMMARIZE = """Summarize the text. Return a well-formatted summary of the following text:
"""
def summarize(text: str) -> str:
    return respond(SUMMARIZE + text, "claude")

TRANSLATE = """Translate the following text to Czech:
Do not mention any details besides the translation itself.
Return all dates and numbers as words instead, as if the text were read by a person instead of written.
Like: "The year 2022" -> "The year two thousand twenty-two" but in Czech ofcourse.
"""

def translate(text: str) -> str:
    return respond(TRANSLATE + text, "r1")

REWORD = """Change the following input text to be formed into sentences instead of points. It should be comprised of whole sentences, that are grammatically correct.
"""
def reword(text: str) -> str:
    return respond(REWORD + text, "r1")
