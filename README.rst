A lightweight wysiwyg editor for Django
=======================================

.. image:: https://pypip.in/download/django-wysiwyg-redactor/badge.png
    :target: https://pypi.python.org/pypi/django-wysiwyg-redactor/
    :alt: Downloads

Screenshot
----------

.. image:: https://raw.githubusercontent.com/douglasmiranda/django-wysiwyg-redactor/master/screenshots/redactor.jpg

What's that
-----------------

*django-wysiwyg-redactor* is a reusable application for Django, using `Redactor WYSIWYG editor <http://redactorjs.com/>`_

Sponsored by `Mess Marketing <http://www.thisismess.com>`_, we use the latest version of redactorjs, always up-to-date.

Dependence
----------

- `Django >= 1.3` # for static files
- `Pillow or PIL` # for image upload

Getting started
---------------

- Install *django-wysiwyg-redactor*:

```pip install django-wysiwyg-redactor```

- Add `'redactor'` to INSTALLED_APPS.

- Add `url(r'^redactor/', include('redactor.urls'))`, to urls.py

- Add default config in settings.py

.. code-block:: python

    REDACTOR_OPTIONS = {'lang': 'en'}
    REDACTOR_UPLOAD = 'uploads/'

More `redactor settings <http://imperavi.com/redactor/docs/settings/>`_.

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

`RedactorEditor` takes the same parameters as `RedactorField`.


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
-  0.4.2 Nov 06, 2014

   -   Fix: "ReferenceError: django is not defined" (pull #54)
   -   Fix: Error in collectstatic post-process (pull #56)
   -   Fix: code block on README

-  0.4.1 oct 21, 2014

   -   REDACTOR 10! o/
   -   Requires jQuery 1.9.*
   -   Some features now are plugins (see redactor docs)
   -   Default: fixed toolbar mode
   -   Bugs fixed, some features removed.
   -   More: http://imperavi.com/redactor/docs/whats-new-10/

-  0.4.0 sep 11, 2014

   -   Great news, now we have an sponsor, which means we can use a up-to-date version of redactorjs. Thanks to @etchalon. ( pull #48 )
   -   Working with python3.4
   -   Update LICENSE
   -   Better error handling

-  0.3.9.1 Jun 06, 2014

   -   Added: Support for custom REDACTOR_FILE_STORAGE ( pull #45 #46 ) Thanks to @pztrick

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

And our awesome sponsor:

Mess Marketing from Chicago, IL
jshedd@thisismess.com
thisismess.com
@etchalon
