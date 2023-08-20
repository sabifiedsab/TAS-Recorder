from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = "A TAS or macro recording tool."
LONG_DESCRIPTION = "A really simple tool for creating tool-assisted content or simple macros"

setup(
    name="tas-recorder",
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        'pynput'
    ],
    author="SabifiedSab",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    keywords=['python', 'tas', 'macro recorder', 'tool assist'],
    license="MIT",
    url="https://github.com/sabifiedsab/tas-recorder",
)
