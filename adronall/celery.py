import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adronall.settings')

app = Celery('adronall')
app.conf.enable_utc=False
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update(timezone='Asia/Kolkata')
# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# celery beat settings
app.conf.beat_scheduler={
# schedular name
# 'send_mail_scheduler':{
#     # call function to perform task
#     'task':'home.task.sendEmailTask',
#     # set time date month
#     'schedule':crontab(hour=1,minute=30),
#     # set arguments
#     # 'args':(2)
# },

# 'send_mail_scheduler2':{
#     # call function to perform task
#     'task':'home.task.sendScheduleEmailTask',
#     # set time date month
#     'schedule':crontab(hour=1,minute=30),
#     # set arguments
#     # 'args':(2)
# }
}

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')