from setuptools import setup

setup(
    name='BuildEverything',
    version='0.1dev',
    packages=['build_everything'],
    license='CC zero',
    long_description=open('README').read(),
    install_requires=[
        'sh',
        ],
    )
