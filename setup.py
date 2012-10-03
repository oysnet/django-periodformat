import os
import codecs
from setuptools import setup, find_packages

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-periodformat',
    version='0.0.1',
    description='Filter helper for date period formating.',
    long_description = read('README.md'),
    author='David Charbonnier',
    author_email='dcharbonnier@gmail.com',
    url = 'https://github.com/oxys-net/django-periodformat',
    download_url='',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe = False,
)