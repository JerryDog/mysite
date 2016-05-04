from __future__ import absolute_import
from mysite import celery_app
import time

@celery_app.task(exchange='django_tasks')
def add():
    time.sleep(20)
    return 20


@celery_app.task(exchange='other_tasks')
def update():
    print "send 2222222222 message"
    time.sleep(5)
    return True
