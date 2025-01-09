import os
from celery import shared_task
from celery.schedules import crontab
from myproject.celery_app.celery import app

@shared_task
def read_prompt_and_save():
    input_file = '/workspace/taskai/myproject/prompts/input_prompt.txt'
    output_file = '/workspace/taskai/myproject/prompts/output_result.txt'
    
    with open(input_file, 'r') as f:
        prompt = f.read().strip()
    
    result = f"Processed prompt: {prompt}"
    
    with open(output_file, 'w') as f:
        f.write(result)
    
    return result

@shared_task
def example_task(x, y):
    return x + y

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute='*/15'),  # Run every 15 minutes
        read_prompt_and_save.s(),
        name='read prompt and save every 15 minutes'
    )