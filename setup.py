from setuptools import setup, find_packages

setup(
    name='cal-auto-python',
    version='0.0.1',
    packages=find_packages(where='src'), 
    package_dir={'': 'src'}, 
    install_requires=[
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib'
    ],
    entry_points={
        'console_scripts': [
            'cal-auto-python=src.main:main',
        ],
    },
)