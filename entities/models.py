from django.db import models
import os
from harpoon2.settings import MANAGER_TYPES, DOWNLOADER_TYPES
from . import managers, downloaders

# Create your models here.


class DownloadFolder(models.Model):
    folder = models.CharField(max_length=400, unique=True)

    def __str__(self):
        return self.folder


class Manager(models.Model):
    name = models.CharField(max_length=30, unique=True)
    managertype = models.CharField(max_length=20, choices=MANAGER_TYPES)
    url = models.URLField()
    apikey = models.CharField(max_length=50)
    folder = models.ForeignKey(DownloadFolder, on_delete=models.CASCADE)
    label = models.CharField(max_length=25)

    @classmethod
    def from_db(cls, db, field_names, values):
        new = super(Manager, cls).from_db(db, field_names, values)
        # cache value went from the base
        new.client = getattr(managers, new.managertype)(new)
        return new


class Downloader(models.Model):
    name = models.CharField(max_length=30, unique=True)
    downloadertype = models.CharField(max_length=20, choices=DOWNLOADER_TYPES)
    options = models.JSONField(default=dict)

    @classmethod
    def from_db(cls, db, field_names, values):
        new = super(Downloader, cls).from_db(db, field_names, values)
        # cache value went from the base
        new.client = getattr(downloaders, new.downloadertype)(new)
        return new

    # @property
    # def client(self):
    #     return getattr(downloaders, self.downloadertype)(self)

    def checkoptions(self):
        optionfields = self.client.optionfields
        for fieldname in optionfields.keys():
            if fieldname not in self.options.keys():
                if optionfields[fieldname] == 'string':
                    self.options[fieldname] = ''
                elif optionfields[fieldname] == 'int':
                    self.options[fieldname] = 0
                elif optionfields[fieldname] == 'boolean':
                    self.options[fieldname] = False
        self.save()

    def test(self):
        if hasattr(self, 'client'):
            if self.client.reload:
                self.client.__init__(self)
            return self.client.test()
