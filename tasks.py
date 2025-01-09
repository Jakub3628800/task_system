from celery_app import app
from lib.claude_api import ClaudeAPI

claude_api = ClaudeAPI()

@app.task
def get_claude_response(prompt):
    return claude_api.get_response(prompt)