import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proud_forest_23287.settings')

app = Celery('proud_forest_23287')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'change_state_on_timer': {
        'task': 'auction.tasks.send_email_on_auction',
        'schedule': 20,
    }
}
