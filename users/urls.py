from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    # path('', views.UserJson.as_view(), name='index'),
    path('<int:userid>/', views.detail, name='detail'),
    path('prefs/', views.userprefs, name='userprefs'),
    ]
