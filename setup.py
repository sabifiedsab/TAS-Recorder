from setuptools import setup, find_packages

setup(
    name="tas-recorder",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'pynput'
    ],
    author="SabifiedSab",
    description="A TAS or macro recording tool.",
    license="MIT",
    url="https://github.com/sabifiedsab/tas-recorder",
)
