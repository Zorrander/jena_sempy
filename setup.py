from setuptools import setup

setup(
    name='jena_sempy',
    version='0.1',
    description='Handle communication between python and Jena triple store',
    author='Alexandre Angleraud',
    author_email='alexandre.angleraud@tuni.fi',
    download_url='https://github.com/Zorrander/jena-sempy/archive/v_0.1.tar.gz',
    license='New BSD License',
    install_requires=[
     'requests'
    ],
    packages=[
     'jena_com'
    ]
)
