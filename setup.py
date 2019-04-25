from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='losant-rest',
    version='1.8.6',
    description='A REST client for the Losant API',
    long_description=long_description,
    url='https://github.com/Losant/losant-rest-python',
    author='Losant',
    author_email='hello@losant.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Topic :: Communications',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    keywords=['REST', 'Losant', 'IoT'],
    test_suite='tests',
    install_requires=['requests>=2.13'],
    tests_require=['requests-mock'],
)
