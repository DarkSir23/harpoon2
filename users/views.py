from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import CustomUserCreationForm, UserPrefsForm
from .models import CustomUser
from django.contrib import messages

def userprefs(request):
    if request.method == 'POST':
        form = UserPrefsForm(request.POST)
        if form.is_valid():
            request.user.email = form.cleaned_data['email']
            request.user.interface = form.cleaned_data['interface']
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.timezone = form.cleaned_data['timezone']
            try:
                request.user.save()
                messages.success(request, "User preferences saved.")
            except Exception as e:
                messages.error(request, "Error: %s" % e)
            return HttpResponseRedirect('/')
    user = get_object_or_404(CustomUser, id=request.user.id)
    session = request.session
    user_sessions = user.get_active_sessions()
    form = UserPrefsForm(instance=user)
    return render(request, 'users/prefs.html', {'form': form, 'session': session, 'user_sessions': user_sessions})


def detail(request, userid):
    try:
        user = CustomUser.objects.get(pk=userid)
    except CustomUser.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'users/detail.html', {'thisuser': user})

