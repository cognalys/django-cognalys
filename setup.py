from setuptools import setup, find_packages

setup(
    name='django-cognalys',
    version='1.1',
    author='Anish menon',
    author_email='anish@inzane.in',
    description='Mobile number verification via missed call . A better replacement for CAPTCHA and verifying mobile number via SMS gateway',
    url='https://github.com/cognalys/django-cognalys',
    license='MIT',
    packages=find_packages(),
    
    classifiers = [
        'Development Status :: Stabe',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django,Flask'
    ]
)
