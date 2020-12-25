from celery import shared_task
from .models import  Item, ItemHistory
from entities.models import Downloader


@shared_task
def queue_cronjob():
    downloaders = Downloader.objects.all()
    for item in Item.objects.filter(downloader_id=None):
        for downloader in downloaders:
            found_client = downloader.client.find_item(item.hash)
            if found_client:
                item.downloader_id = downloader
                item.save()
