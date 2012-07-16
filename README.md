#Version modified of django-redactorjs

I modified things like:

* version of plugin redactorjs 7.6.3 (so this changes the license too)
* add new API method `$('#redactor').getSelection()` get the selected content in editor
* fixing some bugs, adapting things...

If you want to install my version, just install with:

``pip install git+https://github.com/douglasmiranda/django-redactorjs#egg=django-redactorjs``

* Add `'redactor'` to INSTALLED_APPS.

* Add `url(r'^redactor/', include('redactor.urls'))`, to urls.py


Anyway the original README is below.


django-redactorjs
===============
http://github.com/TigorC/django-redactorjs


What's that
-----------

*django-redactorjs is a reusable application for Django, using WYSIWYG editor http://redactorjs.com/*

Dependence
-----------

- `Django >= 1.3` # for static files
- `PIL` # for image upload

Getting started
---------------

* Install django-redactorjs:

``pip install django-redactorjs
``

* Add `'redactor'` to INSTALLED_APPS.

* Add `url(r'^redactor/', include('redactor.urls'))`, to urls.py

* Add default config in settings.py (more settings see: <http://redactorjs.com/docs/settings/>):

```
REDACTOR_OPTIONS = {'lang': 'ru'}
REDACTOR_UPLOAD = 'uploads/'
```

Using in model
--------------


    from django.db import models
    from redactor.fields import RedactorField

    class Entry(models.Model):
        title = models.CharField(max_length=250, verbose_name=u'Заголовок')
        short_text = RedactorField(verbose_name=u'Краткий текст')

or use custom parametrs:

    short_text = RedactorField(
        verbose_name=u'Краткий текст',
        redactor_options={'lang': 'ru', 'focus': 'true'},
        upload_to='tmp/'
    )

Using for only admin interface
-----------------------------
    from django import forms
    from redactor.widgets import RedactorEditor
    from blog.models import Entry

    class EntryAdminForm(forms.ModelForm):
        class Meta:
            model = Entry
            widgets = {
               'short_text': RedactorEditor(),
            }

    class EntryAdmin(admin.ModelAdmin):
        form = EntryAdminForm

`RedactorEditor` takes the same parameters as `RedactorField`

## License 
Starting with version 7.6.2 redactor-js is licensed under [Creative Commons Attribution-NonCommercial 3.0 license](http://creativecommons.org/licenses/by-nc/3.0/)

For commercial use please buy license here: http://redactorjs.com/download/ or use earlier version.