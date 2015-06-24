from setuptools import setup, find_packages

setup(
    name='enaml_hello',
    version='0.1',
    author='Gabriel Reis',
    author_email='gabrielcnr@gmail.com',
    requires=['enaml'],
    packages=find_packages(),
    entry_points={
        'enaml_factories': ['Hello = enaml_hello.qt.qt_hello:hello_factory'],
    },
)
