"""Setup for multilanguage XBlock."""

import os
from setuptools import setup


def package_data(pkg, root):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for dirname, _, files in os.walk(os.path.join(pkg, root)):
        for fname in files:
            data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='multilanguage-xblock',
    version='0.5',
    description='multilanguage XBlock',   # TODO: write a better description.
    packages=[
        'multilanguage',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'multilanguage = multilanguage:MultiLanguageXBlock',
        ]
    },
    package_data=package_data("multilanguage", "static"),
)