from setuptools import setup

import stockcodes
import sendmail

long_desc = """
stockcodes
sendmail
"""

setup(
        name='easypub',
        description='easypub',
        long_description=long_desc,
        author='oldwain',
        author_email='oldwain@163.com',
        license='BSD',
        url='https://github.com/oldwain/easypub',
        keywords='China stock codes',
        install_requires=['requests'],
        classifiers=['Development Status :: 4 - Beta',
                     'Programming Language :: Python :: 3.5',
                     'License :: OSI Approved :: BSD License'],
        packages=['stockcodes','sendmail'],
        package_data={'': ['*.conf']}
)
