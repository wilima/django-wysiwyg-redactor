import os
from setuptools import setup
from redactor import VERSION

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='django-wysiwyg-redactor',
    version=".".join(map(str, VERSION)),
    description='This reusable Django app using WYSIWYG editor redactorjs.com',
    long_description=readme,
    author="Douglas Miranda",
    author_email='douglasmirandasilva@gmail.com',
    url='https://github.com/douglasmiranda/django-wysiwyg-redactor',
    packages=['redactor'],
    include_package_data=True,
    install_requires=['setuptools'],
    zip_safe=False,
    classifiers=[
    'Development Status :: 4.5 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
