import json
from django.conf import settings
from django.utils.translation import ugettext as _
from django.http import HttpResponse
from django.views.generic import FormView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import force_str

from redactor.forms import ImageForm
from redactor.utils import import_class, is_module_image_installed


class RedactorUploadView(FormView):
    form_class = ImageForm
    http_method_names = ('post',)
    upload_to = getattr(settings, 'REDACTOR_UPLOAD', 'redactor/')
    upload_handler = getattr(settings, 'REDACTOR_UPLOAD_HANDLER',
                             'redactor.handlers.SimpleUploader')

    @method_decorator(csrf_exempt)
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        if not is_module_image_installed():
            data = {
                'error': _("ImproperlyConfigured: Neither Pillow nor PIL could be imported: No module named 'Image'"),
            }
            return HttpResponse(json.dumps(data),
                                content_type='application/json')

        return super(RedactorUploadView, self).dispatch(request, *args,
                                                        **kwargs)

    def form_invalid(self, form):
        try:
            error = form.errors.values()[-1][-1]
        except:
            error = _('Invalid file.')
        data = {
            'error': error,
        }
        return HttpResponse(json.dumps(data), content_type='application/json')

    def form_valid(self, form):
        file_ = form.cleaned_data['file']
        handler_class = import_class(self.upload_handler)
        uploader = handler_class(file_)
        uploader.save_file()
        file_name = force_str(uploader.get_filename())
        file_url = force_str(uploader.get_url())
        data = {
            'filelink': file_url,
            'filename': file_name,
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
