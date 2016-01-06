from setuptools import setup

setup(
    name='textkit',
    version='0.0.1',
    py_modules=['textkit'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        textkit=textkit.cli:cli
    ''',
)
