import json
from django import forms
from django.forms import widgets
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.conf import settings


GLOBAL_OPTIONS = getattr(settings, 'REDACTOR_OPTIONS', {})


class RedactorEditor(widgets.Textarea):
    init_js = '''<script type="text/javascript">
                    jQuery(document).ready(function(){
                        var $field = jQuery("#%s");
                        options = %s;
                        options.imageUploadErrorCallback = function(json){
                            alert(json.error);
                        };
                        $field.redactor(options);
                    });
                 </script>
              '''

    def __init__(self, *args, **kwargs):
        self.upload_to = kwargs.pop('upload_to', '')
        self.custom_options = kwargs.pop('redactor_options', {})
        self.allow_file_upload = kwargs.pop('allow_file_upload', True)
        self.allow_image_upload = kwargs.pop('allow_image_upload', True)
        super(RedactorEditor, self).__init__(*args, **kwargs)

    def get_options(self):
        options = GLOBAL_OPTIONS.copy()
        options.update(self.custom_options)
        if self.allow_file_upload:
            options['fileUpload'] = reverse(
                'redactor_upload_file',
                kwargs={'upload_to': self.upload_to}
            )
        if self.allow_image_upload:
            options['imageUpload'] = reverse(
                'redactor_upload_image',
                kwargs={'upload_to': self.upload_to}
            )
        return json.dumps(options)

    def render(self, name, value, attrs=None):
        html = super(RedactorEditor, self).render(name, value, attrs)
        final_attrs = self.build_attrs(attrs)
        id_ = final_attrs.get('id')
        html += self.init_js % (id_, self.get_options())
        return mark_safe(html)

    def _media(self):
        js = (
            'redactor/jquery.redactor.init.js',
            'redactor/redactor.js',
            'redactor/langs/{0}.js'.format(GLOBAL_OPTIONS.get('lang', 'en')),
        )
        css = {
            'all': (
                'redactor/css/redactor.css',
                'redactor/css/django_admin.css',
            )
        }
        return forms.Media(css=css, js=js)
    media = property(_media)
