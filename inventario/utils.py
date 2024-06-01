from django.conf import settings
from django.contrib.staticfiles import finders
import os

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    if uri.startswith(settings.MEDIA_URL):
        path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    elif uri.startswith(settings.STATIC_URL):
        path = finders.find(uri.replace(settings.STATIC_URL, ""))
        if not path:
            raise Exception('File {} not found in STATICFILES_DIRS.'.format(uri))
    else:
        return uri

    if not os.path.isfile(path):
        raise Exception('Media URI must start with {} or {}'.format(settings.STATIC_URL, settings.MEDIA_URL))

    return path