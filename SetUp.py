# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='OSGIFI',
    version="0.1",
    packages=find_packages(),
    author="okr3vl",
    install_requires=["argparse","tabulate","httpx","tqdm","unicodecsv","requests","colorama"],
    description="This tool permit you to gathering information from instagram accounts such as Phone Number, E-mail, ID on Instagram Accounts via API.",
    long_description="This tool permit you to gathering information from instagram accounts such as Phone Number, E-mail, ID on Instagram Accounts via API.",
    include_package_data=True,
    url='http://github.com/okr3vl/OSGIFI',
    entry_points = {'console_scripts': ['OSGIFI = OSGIFI.core:main']},
    classifiers=[
        "Language :: Python",
    ],
)
