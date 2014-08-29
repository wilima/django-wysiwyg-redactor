try:
    from django.conf.urls import url, patterns
except ImportError:
    # for Django version less than 1.4
    from django.conf.urls.defaults import url, patterns

from redactor.views import RedactorUploadView
from redactor.forms import FileForm, ImageForm


urlpatterns = patterns(
    '',
    url('^upload/image/(?P<upload_to>.*)',
        RedactorUploadView.as_view(form_class=ImageForm),
        name='redactor_upload_image'),

    url('^upload/file/(?P<upload_to>.*)',
        RedactorUploadView.as_view(form_class=FileForm),
        name='redactor_upload_file'),
)
