from .models import CustomUser
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib import messages
from django.utils import timezone

@receiver(user_logged_in, sender=CustomUser)
def logged_in(sender, request, user, **kwargs):
    request.session['last_login'] = timezone.now().isoformat()
    source = '%s (%s)' % (request.META['REMOTE_HOST'], request.META['REMOTE_ADDR'])
    request.session['login_source'] = source
    request.session['login_agent'] = request.META['HTTP_USER_AGENT']
    request.session.modified=True
    print(request.META)
