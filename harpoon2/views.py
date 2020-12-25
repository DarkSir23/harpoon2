from django.shortcuts import get_object_or_404, render
from entities.models import Manager

def home(request):
    managers = Manager.objects.all()
    return render(request, 'home.html', {'managers': managers})