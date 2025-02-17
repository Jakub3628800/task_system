from celery import Celery
from lib.llm import summarize, translate, reword
from lib.tts import create_tts_from_text
from lib.browser import visit_site

app = Celery('tasks')
app.conf.update(
    broker_url='redis://localhost:6379/0',
    result_backend='redis://localhost:6379/0',
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
)
app.conf.worker_send_task_events = True  # Enables task events
app.conf.task_send_sent_event = True  # Enables sent events
app.conf.task_track_started = True  # (opt) Update task result state to STARTED
app.conf.result_extended = True  # (opt) Store args and kwargs in the result

@app.task(name="llm.summarize")
def summarize_text(text: str) -> str:
    """Task for summarizing text using LLM"""
    return summarize(text)

@app.task(name="llm.translate")
def translate_text(text: str) -> str:
    """Task for translating text to Czech using LLM"""
    return translate(text)

@app.task(name="llm.reword")
def reword_text(text: str) -> str:
    """Task for rewording text into sentences using LLM"""
    return reword(text)

@app.task(name="tts.create_speech")
def create_speech(text: str) -> str:
    """Task for converting text to speech"""
    return create_tts_from_text(text)

@app.task(name="browser.visit_site")
def visit_website(url: str) -> str:
    """Task for visiting a website and returning its content"""
    return visit_site(url)

@app.task(name="browser.visit_and_summarize")
def visit_and_summarize(url: str) -> str:
    """Visit a website and summarize its content"""
    # Get full website content
    content = visit_website(url)
    # Generate summary from content
    return summarize_text(content)

