from setuptools import setup, find_packages

with open('README.rst', encoding = 'UTF-8') as f:
    readme = f.read()

setup(
    name = 'hr',
    version = '1.0.0',
    description = 'Command line user export utility',
    long_description = readme,
    long_description_content_type = 'text/markdown',
    author = 'Damian Ramirez',
    author_email = 'dramirez@edrans.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = [],
    python_requires = '>=3.10',
    entry_points = {
        'console_scripts': [
            'hr=hr.cli:main'
        ],
    }
)