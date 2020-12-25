from django.contrib.auth.models import AbstractUser
from django.db import models
from harpoon2.settings import THEMES
from django.urls import reverse
from dplibs.session import clear_inactive_sessions, get_sessions
import pytz

def timezone_choices():
    choices = []
    for zone in pytz.common_timezones:
        choices.append((zone, zone))
    return choices


class CustomUser(AbstractUser):
    interface = models.CharField(max_length=20, blank=True, choices=THEMES)
    prefs = models.CharField(max_length=200, blank=True)
    timezone = models.CharField(max_length=40, blank=True, choices=timezone_choices())

    # add additional fields in here

    def __str__(self):
        return self.username

    def get_active_sessions(self):
        clear_inactive_sessions()
        user_sessions = get_sessions(userid=self.id)
        return user_sessions

    def get_active_session_count(self):
        return len(self.get_active_sessions())

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'userid': self.pk})

    def get_link(self):
        return f'<a href={self.get_absolute_url()}>{self.username}</a>'