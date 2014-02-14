A lightweight wysiwyg editor for Django
=======================================

Some changes:

- redactorjs 7.6.3 (changes the [license](#license) too)
- new API methods 
    - `$('#redactor').getSelection()` get the selected content in editor
    - `$('#redactor').getSettings()` you can get and set settings anytime you want
- removing some ajax calls, (modal windows), to avoid the crossdomain issue on production env
- with the *extra_script* option/setting you can load some script to do something more after load the redactor
- now the redactor toolbar is more responsive
- fixing some bugs, adapting things...

Screenshot
-----------------

.. image:: https://raw.github.com/douglasmiranda/django-wysiwyg-redactor/master/static/img/screenshot.png

What's that
-----------------

*django-wysiwyg-redactor* is a reusable application for Django, using `Redactor WYSIWYG editor <http://redactorjs.com/>`_

Dependence
-----------------

- `Django >= 1.3` # for static files
- `PIL` # for image upload

Getting started
-----------------

- Install *django-wysiwyg-redactor*:

```pip install django-wysiwyg-redactor```

- Add `'redactor'` to INSTALLED_APPS.

- Add `url(r'^redactor/', include('redactor.urls'))`, to urls.py

- Add default config in settings.py (fot more settings, see `here <https://github.com/douglasmiranda/django-wysiwyg-redactor/wiki/Settings>`_)

```
REDACTOR_OPTIONS = {'lang': 'en'}
REDACTOR_UPLOAD = 'uploads/'
```



Using in model
-----------------
this:
::
 from django.db import models
 from redactor.fields import RedactorField

 class Entry(models.Model):
     title = models.CharField(max_length=250, verbose_name=u'Title')
     short_text = RedactorField(verbose_name=u'Text')

or use custom parametrs:
::
 short_text = RedactorField(
     verbose_name=u'Text',
     redactor_options={'lang': 'en', 'focus': 'true'},
     upload_to='tmp/',
     allow_file_upload=True,
     allow_image_upload=True
 )

Using for only admin interface
------------------------------
this:
::
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

Contributing
-----------------

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request =]

History
-------
-  0.3.8.2 Feb 14, 2014

   -   Improvement: Rename uploaded image by dint of uuid ( pull #33 )

-  0.3.8.1 Feb 13, 2014

   -   Fix: Solve Deprecation of 'simplejson' ( pull #25 )

-  previous versions

   -   Lots of fixes, see the commits.

Who is behind this?
-------------------
Awesome people, you should see the `AUTHORS <https://github.com/douglasmiranda/django-wysiwyg-redactor/blob/master/AUTHORS>`_ file.

License
-----------------
Starting with version 7.6.3 redactor-js is licensed under `Creative Commons Attribution-NonCommercial 3.0 license <http://creativecommons.org/licenses/by-nc/3.0/>`_

If you want to use a newer version please buy license `here <http://imperavi.com/redactor/download>`_
