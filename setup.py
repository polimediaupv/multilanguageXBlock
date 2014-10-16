"""Setup for multitab XBlock."""

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
    name='multitab-xblock',
    version='0.4',
    description='multitab XBlock',   # TODO: write a better description.
    packages=[
        'multitab',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'multitab = multitab:MultiTabXBlock',
        ]
    },
    package_data=package_data("multitab", "static"),
)