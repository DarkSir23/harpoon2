from harpoon2 import settings
from _version import __version__
import sys

def custom_proc(request):
    # A context processor that provides 'app', 'user' and 'ip_address'.
    if request.user.is_authenticated:
        interface = request.user.interface if request.user.interface else settings.INTERFACE
    else:
        interface = settings.INTERFACE

    return {
        'brandingname': 'Harpoon',
        'interface': interface,
        'ip_address': request.META['REMOTE_ADDR'],
        'version': __version__,
    }