from django.shortcuts import render
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView
from django.urls import reverse_lazy, reverse
from .models import DownloadFolder, Manager
from .forms import DLFolderModalForm, ManagerModalForm
from .managers import Arr, Sonarr, Radarr, Lidarr, Readarr

# Create your views here.

class DLFolderCreateView(BSModalCreateView):
    model = DownloadFolder
    template_name = 'entities/dlfoldercreate.html'
    form_class = DLFolderModalForm
    success_message = 'Download folder added.'
    success_url = reverse_lazy('entities:settings')


class ManagerCreateView(BSModalCreateView):
    model = Manager
    template_name = 'entities/managercreate.html'
    form_class = ManagerModalForm
    success_message = 'Manager successfully created.'
    success_url = reverse_lazy('entities:managers')


class ManagerUpdateView(BSModalUpdateView):
    model = Manager
    template_name = 'entities/managercreate.html'
    form_class = ManagerModalForm
    success_message = 'Manager successfully modified.'
    success_url = reverse_lazy('entities:managers')


def settings(request):
    folders = DownloadFolder.objects.all()
    return render(request, 'entities/settings.html', {'folders': folders})

def managers(request):
    managers = Manager.objects.all()
    return render(request, 'entities/managers.html', {'managers': managers})

def managertest(request, pk):
    manager = Manager.objects.get(pk=pk)
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