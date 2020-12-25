from django.db import models
# from entities.models import Manager, Downloader
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200, default='', blank=True)
    hash = models.CharField(max_length=50, primary_key=True)
    manager = models.ForeignKey('entities.Manager', on_delete=models.CASCADE, null=True, blank=True)
    downloader = models.ForeignKey('entities.Downloader', on_delete=models.CASCADE, null=True, blank=True)
    size = models.BigIntegerField(default=0)
    received = models.BigIntegerField(default=0)
    status = models.CharField(max_length=50, default='Created')
    clientid = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class ItemHistory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='history')
    created = models.DateTimeField(auto_now_add=True)
    details = models.CharField(max_length=200)