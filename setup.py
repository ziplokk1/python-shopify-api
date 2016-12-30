from setuptools import setup, find_packages

version = '0.1.3'

REQUIREMENTS = [
    'python-dateutil',
    'requests'
]

setup(
    name='python-shopify',
    version=version,
    packages=find_packages(),
    url='https://github.com/ziplokk1/python-shopify-api',
    license='LICENSE.txt',
    author='Mark Sanders',
    author_email='sdscdeveloper@gmail.com',
    install_requires=REQUIREMENTS,
    description='Wrapper and parser modules for Shopify\'s API.',
    include_package_data=True
)
