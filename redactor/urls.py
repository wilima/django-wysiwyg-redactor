try:
    from django.conf.urls import url, patterns
except ImportError:
    # for Django version less than 1.4
    from django.conf.urls.defaults import url, patterns

from redactor.views import redactor_upload
from redactor.forms import FileForm, ImageForm


urlpatterns = patterns(
    '',
    url('^upload/image/(?P<upload_to>.*)', redactor_upload,
        {
            'form_class': ImageForm,
            'response': lambda name, url: '<img src="{0}" alt="{1}" />'.format(
                url,
                name
            ),
        },
        name='redactor_upload_image'),

    url('^upload/file/(?P<upload_to>.*)', redactor_upload,
        {
            'form_class': FileForm,
            'response': lambda name, url: '<a href="{0}">{1}</a>'.format(url,
                                                                         name),
        },
        name='redactor_upload_file'),
)
