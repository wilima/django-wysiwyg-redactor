A lightweight wysiwyg editor for Django
=======================================

.. image:: https://pypip.in/download/django-wysiwyg-redactor/badge.png
    :target: https://pypi.python.org/pypi/django-wysiwyg-redactor/
    :alt: Downloads

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
----------

.. image:: https://raw.github.com/douglasmiranda/django-wysiwyg-redactor/master/static/img/screenshot.png

What's that
-----------------

*django-wysiwyg-redactor* is a reusable application for Django, using `Redactor WYSIWYG editor <http://redactorjs.com/>`_

Dependence
----------

- `Django >= 1.3` # for static files
- `PIL` # for image upload

Getting started
---------------

- Install *django-wysiwyg-redactor*:

```pip install django-wysiwyg-redactor```

- Add `'redactor'` to INSTALLED_APPS.

- Add `url(r'^redactor/', include('redactor.urls'))`, to urls.py

- Add default config in settings.py (fot more settings, see `here <https://github.com/douglasmiranda/django-wysiwyg-redactor/wiki/Settings>`_)

.. code-block:: python

    REDACTOR_OPTIONS = {'lang': 'en'}
    REDACTOR_UPLOAD = 'uploads/'



Using in model
--------------

.. code-block:: python

    from django.db import models
    from redactor.fields import RedactorField

    class Entry(models.Model):
        title = models.CharField(max_length=250, verbose_name=u'Title')
        short_text = RedactorField(verbose_name=u'Text')

or use custom parametrs:

.. code-block:: python

    short_text = RedactorField(
        verbose_name=u'Text',
        redactor_options={'lang': 'en', 'focus': 'true'},
        upload_to='tmp/',
        allow_file_upload=True,
        allow_image_upload=True
    )

Using for only admin interface
------------------------------

.. code-block:: python
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


Upload Handlers
---------------
SimpleUploader - The Standard Uploader. Will upload your file to REDACTOR_UPLOAD.

UUIDUploader - This handler will replace the original file name for an UUID.

DateDirectoryUploader - This handler saves the file in a directory based on the current server date.

Usage:

For example, if I want to use the DateDirectoryUploader handler, I will put this on settings.py:

.. code-block:: python

    REDACTOR_UPLOAD_HANDLER = 'redactor.handlers.DateDirectoryUploader'


File Storages
-------------
*django-wysiwyg-redactor* defaults to using the default media storage for your Django application.

This can be overriden to use a different storage backend with this settings.py variable:

.. code-block::

    REDACTOR_FILE_STORAGE = 'my_site.file_storages.storage_instance'

Information on writing a custom storage backend is `here in the Django documentation <https://docs.djangoproject.com/en/1.7/howto/custom-file-storage/>`_.

Other third-party libraries exist to provide storage backends for cloud object storages (e.g. `django-cumulus <https://github.com/django-cumulus/django-cumulus/>`_ for Rackspace/OpenStack or `django-storages <http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html>`_ for Amazon S3).


NOTE: Soon we will have a better documentation.

Contributing
------------

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request =]

History
-------
-  0.3.9 Mar 29, 2014

   -   New Feature: Upload Handler (pull #43) Special Thanks to @SilentSokolov
   -   Fix unicode filename issue.

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
-------
Starting with version 7.6.3 redactor-js is licensed under `Creative Commons Attribution-NonCommercial 3.0 license <http://creativecommons.org/licenses/by-nc/3.0/>`_

If you want to use a newer version please buy license `here <http://imperavi.com/redactor/download>`_
