from setuptools import setup

setup(
    name='BuildEverything',
    version='0.1dev',
    packages=['build_everything'],
    license='CC zero',
    long_description=open('README').read(),
    install_requires=[
        'sh',
        'PyYAML',
        ],
    entry_points = {
        'console_scripts': [
            'build_one = build_everything:build_one_main',
            'test_sample_projects = build_everything:test_sample_projects_main',
            ]},
    package_data = {
        'rules': ['*.yaml'],
        }
    )
