import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as README:
    long_description = README.read()

setup(
    name='Flask Debug API',
    version='0.0.1',
    url='http://github.com/kevinbeaty/flask-debug-api',
    license='MIT',
    author='Kevin Beaty',
    author_email='kevin@simplectic.com',
    description='API Browser for Flask-DebugToolbar',
    long_description=long_description,
    packages=['flask_debug_api'],
    include_package_data=False,
    zip_safe=False,
    platforms='any',
    install_requires=['Flask-DebugToolbar'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup'],
    cmdclass={},
    test_suite=''
)
