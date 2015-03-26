#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="django-intensedebate",
    version="0.6.0",
    author="Raymond Wanyoike",
    author_email="raymond.wanyoike@gmail.com",
    url="https://github.com/raymondwanyoike/django-intensedebate/",
    description="Simple integration of the IntenseDebate comment widget for " +
        "Django projects.",
    long_description=open("README.rst").read(),
    download_url="https://github.com/raymondwanyoike/django-intensedebate/",
    license="GPLv3",
    packages=find_packages(),
    include_package_data=True,
    keywords="django, intensedebate",
    install_requires=[
        "Django>=1.4,<=1.6.11",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities",
    ],
    zip_safe=False,
)
