import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'harpoon2.settings')

app = Celery('harpoon2')
#app.config_from_object('harpoon2.settings')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'run-entity_cronjob': {
        'task': 'entities.tasks.queue_cronjob',
        'schedule': crontab(),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
    'run-queue_cronjob': {
        'task': 'itemqueue.tasks.queue_cronjob',
        'schedule': crontab(),
    }
}