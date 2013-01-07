#/usr/bin/env python
from setuptools import setup, find_packages
import os

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)


setup(
    name="django-foundation",
    version="0.1",
    description="Django Integration with foundation front-end.",
    author="Marcos Daniel Petry",
    author_email="marcospetry@gmail.com",
    url="https://github.com/petry/django-foundation",
    license='BSD License', 
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
