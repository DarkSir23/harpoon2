from django.shortcuts import render
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView
from django.urls import reverse_lazy, reverse
from . import forms
from . import models
from .managers import Arr, Sonarr, Radarr, Lidarr, Readarr

# Create your views here.

class DLFolderCreateView(BSModalCreateView):
    model = models.DownloadFolder
    template_name = 'entities/dlfoldercreate.html'
    form_class = forms.DLFolderModalForm
    success_message = 'Download folder added.'
    success_url = reverse_lazy('entities:settings')


class ManagerCreateView(BSModalCreateView):
    model = models.Manager
    template_name = 'entities/managercreate.html'
    form_class = forms.ManagerModalForm
    success_message = 'Manager successfully created.'
    success_url = reverse_lazy('entities:managers')


class ManagerUpdateView(BSModalUpdateView):
    model = models.Manager
    template_name = 'entities/managercreate.html'
    form_class = forms.ManagerModalForm
    success_message = 'Manager successfully modified.'
    success_url = reverse_lazy('entities:managers')


class DownloaderCreateView(BSModalCreateView):
    model = models.Downloader
    template_name = 'entities/downloadercreate.html'
    form_class = forms.DownloaderModalForm
    success_message = 'Downloader successfully created.'
    success_url = reverse_lazy('entities:downloaders')


class DownloaderUpdateView(BSModalUpdateView):
    model = models.Downloader
    template_name = 'entities/downloadercreate.html'
    form_class = forms.DownloaderModalForm
    success_message = 'Downloader successfully modified.'
    success_url = reverse_lazy('entities:downloaders')


def settings(request):
    folders = models.DownloadFolder.objects.all()
    return render(request, 'entities/settings.html', {'folders': folders})

def managers(request):
    managers = models.Manager.objects.all()
    return render(request, 'entities/managers.html', {'managers': managers})

def downloaders(request):
    downloaders = models.Downloader.objects.all()
    return render(request, 'entities/downloaders.html', {'downloaders': downloaders})

def managertest(request, pk):
    manager = models.Manager.objects.get(pk=pk)
    if manager.managertype in ['Sonarr', 'Radarr', 'Lidarr', 'Readarr']:
        if manager.managertype == 'Sonarr':
            client = Sonarr(manager)
        elif manager.managertype == 'Radarr':
            client = Radarr(manager)
        elif manager.managertype == 'Readarr':
            client = Readarr(manager)
        else:
            client = Lidarr(manager)
        success, message = client.test()
        return render(request, 'entities/clienttest.html', {'success': success, 'message': message, 'manager': manager})