from django.urls import path
from . import views

app_name = 'entities'
urlpatterns = [
    path('dlfoldercreate/', views.DLFolderCreateView.as_view(), name='dlfolder-create'),
    path('managercreate/', views.ManagerCreateView.as_view(), name='manager-create'),
    path('downloadercreate/', views.DownloaderCreateView.as_view(), name='downloader-create'),
    path('managers/<int:pk>/update/', views.ManagerUpdateView.as_view(), name='manager-update'),
    path('settings/', views.settings, name='settings'),
    path('managers/', views.managers, name='managers'),
    path('downloaders/', views.downloaders, name='downloaders'),
    path('managers/<int:pk>/test/', views.managertest, name='manager-test'),
]