from celery_app.celery import app
from time import sleep

@app.task(name='tasks.long_process')
def long_process(duration):
    """
    A task that simulates a time-consuming process
    """
    sleep(duration)
    return f"Task completed after {duration} seconds"

@app.task(name='tasks.process_with_retry',
          bind=True,
          max_retries=3,
          default_retry_delay=5)
def process_with_retry(self, value):
    """
    A task that demonstrates retry mechanism
    """
    try:
        if value < 0:
            raise ValueError("Value cannot be negative")
        return f"Successfully processed value: {value}"
    except ValueError as exc:
        return self.retry(exc=exc)


