from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio

from browser_use import BrowserConfig

config = BrowserConfig(
    headless=True,
    disable_security=True
)

# Initialize the model
#api_key = os.getenv("DEEPSEEK_API_KEY")
#llm=ChatOpenAI(base_url='https://api.deepseek.com/v1', model='deepseek-chat', api_key=SecretStr(api_key))


llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.0,
)


async def main(task: str):
    agent = Agent(
        task=task,
        llm=llm,
        use_vision=False
    )
    result = await agent.run()
    return result.final_result()


VISIT_SITE = """
visit site and return it's content. Return it's content fully without summarizing. No html tags but full content of the text
"""

def visit_site(url: str) -> str:
    task = VISIT_SITE + url

    return asyncio.run(main(task))
