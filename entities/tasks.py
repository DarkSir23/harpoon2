from harpoon2.celery import app
from celery import shared_task
from .models import Manager
import logging

@shared_task
def queue_cronjob():
    for manager in Manager.objects.all():
        status, results = manager.client.check_queue()
        if results:
            for result in results:
                manager.client.check_itemqueue(result)
