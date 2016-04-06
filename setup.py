from setuptools import setup

import stockcodes

long_desc = """
stockcodes
"""

setup(
        name='stockcodes',
        description='stockcodes',
        long_description=long_desc,
        author='oldwain',
        author_email='oldwain@163.com',
        license='BSD',
        url='https://github.com/oldwain/stockcodes',
        keywords='China stock codes',
        install_requires=['requests'],
        classifiers=['Development Status :: 4 - Beta',
                     'Programming Language :: Python :: 3.5',
                     'License :: OSI Approved :: BSD License'],
        packages=['stockcodes'],
        package_data={'': ['*.conf']}
)
