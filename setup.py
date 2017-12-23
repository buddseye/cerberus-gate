import os
from setuptools import setup, find_packages

base_dir_path = os.path.dirname(__file__)
readme_file_path = os.path.join(base_dir_path, 'README.md')
requirements_file_path = os.path.join(base_dir_path, 'requirements.txt')

long_description = open(readme_file_path).read()
requirements = open(requirements_file_path).readlines()

setup(
    name='cerberus-gate',
    version='0.0.1',
    description='Data validation cli tool using cerberus.',
    author='buddseye',
    author_email='hokurodaibutu@live.jp',
    url='https://github.com/buddseye/cerberus-gate',
    install_requires=requirements,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cgate=cgate.cgate:main',
        ],
    },
)