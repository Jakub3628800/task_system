# tasks.py
from celery import Celery
from celery.signals import worker_ready

# Create the Celery app with Redis broker
# Using the same Redis configuration as in docker-compose
app = Celery(
        'something',
        broker='redis://localhost:6379/0',
        backend='redis://localhost:6379/0'
        )

# Configure Celery
app.conf.update(
    
    # Task settings
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    
    # Broker connection retry settings
    broker_connection_retry=True,
    broker_connection_retry_on_startup=True,
    broker_connection_max_retries=100,
    
    # Event settings (matching your Leek configuration)
    worker_send_task_events=True,
)

@app.task(name='example.add')
def add(x, y):
    ## this tasks will also create a test file
    with open('test.txt', 'w') as f:
        f.write('This is a test file')
    return x + y

