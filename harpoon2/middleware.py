from django.utils import timezone
import pytz
from harpoon2.settings import TIME_ZONE
from django.utils.deprecation import MiddlewareMixin


class UserTimeZone(MiddlewareMixin):

    def process_request(self, request):
        if request.user.is_authenticated:
            timezone_selected = request.user.timezone
            if not timezone_selected:
                timezone_selected = TIME_ZONE
            timezone.activate(pytz.timezone(timezone_selected))
        else:
            timezone.deactivate()
