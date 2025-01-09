from celery import Celery
from myproject.config.settings import settings

app = Celery('myproject')
app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks(['myproject.tasks'])

if __name__ == '__main__':
    app.start()