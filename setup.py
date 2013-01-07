#/usr/bin/env python
import os
from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)


setup(
    name="django-foundation",
    version="0.1",
    description="Powerful image management for the Django web framework.",
    author="Marcos Daniel Petry",
    author_email="marcospetry@gmail.com",
    url="https://github.com/petry/django-foundation",
    license='Apache License 2.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
    install_requires=[
        #'Django>=1.3',
    ],
)
