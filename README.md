# django-wysiwyg-redactor - A lightweight wysiwyg editor

(Modified version of django-redactorjs)

Some changes:

* redactorjs 7.6.3 (changes the [license](#license) too)
* new API methods 
    * `$('#redactor').getSelection()` get the selected content in editor
    * `$('#redactor').getSettings()` you can get and set settings anytime you want
* removing some ajax calls, (modal windows), to avoid the crossdomain issue on production env
* with the *extra_script* option/setting you can load some script to do something more after load the redactor
* now the redactor toolbar is more responsive
* fixing some bugs, adapting things...

<a href="https://crate.io/packages/django-wysiwyg-redactor/"><img src="https://pypip.in/d/django-wysiwyg-redactor/badge.png"></a>

## Screenshot

<img src="https://raw.github.com/douglasmiranda/django-wysiwyg-redactor/master/static/img/screenshot.png">

What's that
-----------

*django-wysiwyg-redactor is a reusable application for Django, using WYSIWYG editor http://redactorjs.com/*

Dependence
----------

- `Django >= 1.3` # for static files
- `PIL` # for image upload

Getting started
---------------

* Install django-wysiwyg-redactor:

```
pip install django-wysiwyg-redactor
```

* Add `'redactor'` to INSTALLED_APPS.

* Add `url(r'^redactor/', include('redactor.urls'))`, to urls.py

* Add default config in settings.py (more settings here: <https://github.com/douglasmiranda/django-wysiwyg-redactor/wiki/Settings>):

```python
REDACTOR_OPTIONS = {'lang': 'en'}
REDACTOR_UPLOAD = 'uploads/'
```

Using in model
--------------

```python
from django.db import models
from redactor.fields import RedactorField

class Entry(models.Model):
    title = models.CharField(max_length=250, verbose_name=u'Title')
    short_text = RedactorField(verbose_name=u'Text')
```
or use custom parametrs:
```python
    short_text = RedactorField(
        verbose_name=u'Text',
        redactor_options={'lang': 'en', 'focus': 'true'},
        upload_to='tmp/',
        allow_file_upload=True,
        allow_image_upload=True
    )
```
Using for only admin interface
------------------------------
```python
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
```

`RedactorEditor` takes the same parameters as `RedactorField`

## License 
Starting with version 7.6.3 redactor-js is licensed under [Creative Commons Attribution-NonCommercial 3.0 license](http://creativecommons.org/licenses/by-nc/3.0/)

For commercial use please buy license here: http://redactorjs.com/download/ or use earlier version.