try:
    from django.conf.urls import url, patterns, include
except ImportError:
    # for Django version less than 1.4
    from django.conf.urls.defaults import url, patterns, include

from redactor.views import redactor_upload
from redactor.forms import FileForm, ImageForm


urlpatterns = patterns(
    '',
    url('^upload/image/(?P<upload_to>.*)', redactor_upload, {
        'form_class': ImageForm,
        'response': lambda name, url: '<img src="%s" alt="%s" />' % (url, name),
        }, name='redactor_upload_image'),

    url('^upload/file/(?P<upload_to>.*)', redactor_upload, {
        'form_class': FileForm,
        'response': lambda name, url: '<a href="%s">%s</a>' % (url, name),
        }, name='redactor_upload_file'),
)
